"""Validate LLM config in config.json and .env, with optional live API test."""
import asyncio
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def load_dotenv(path: Path) -> dict:
    """Minimal .env parser (key=value, # comments, no variable expansion)."""
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip("\"'")
        env[key] = val
    return env


def check(label: str, ok: bool, detail: str = ""):
    tag = "✔" if ok else "✘"
    print(f"  {tag}  {label}" + (f"  ({detail})" if detail else ""))


def main():
    errors = 0
    print(f"\n{'='*50}")
    print("  Horizon LLM 配置检查")
    print(f"{'='*50}\n")

    # ── 1. .env ──────────────────────────────────────────────
    print("1. 环境变量 (.env)")
    dotenv_path = PROJECT_ROOT / ".env"
    check(".env 文件存在", dotenv_path.exists())
    if not dotenv_path.exists():
        errors += 1
        print("\n  提示: 复制 .env.example 为 .env 并填入密钥")
        print(f"        cp {PROJECT_ROOT}/.env.example {dotenv_path}\n")

    dotenv_vars = load_dotenv(dotenv_path)
    # Save into os.environ so python-dotenv would see them
    for k, v in dotenv_vars.items():
        os.environ.setdefault(k, v)

    # Check common key patterns
    for var in ["LLM_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY",
                "AZURE_OPENAI_API_KEY", "GOOGLE_API_KEY", "MINIMAX_API_KEY",
                "DASHSCOPE_API_KEY"]:
        val = os.getenv(var)
        check(f"${var} {'已设置' if val else '未设置'}", bool(val),
              f"{val[:12]}..." if val and len(val) > 12 else (val or ""))

    # Unified LLM overrides
    for var in ["LLM_BASE_URL", "LLM_MODEL"]:
        val = os.getenv(var)
        if val:
            check(f"${var} 已覆写", True, val)

    # ── 2. config.json ───────────────────────────────────────
    print("\n2. 运行时配置 (data/config.json)")
    config_path = PROJECT_ROOT / "data" / "config.json"
    check("config.json 文件存在", config_path.exists())
    if not config_path.exists():
        errors += 1
        print("   ✘ 中止: 缺少 config.json，运行 horizon-wizard 创建")
        sys.exit(1)

    try:
        raw = json.loads(config_path.read_text())
    except json.JSONDecodeError as e:
        check("config.json 是合法 JSON", False, str(e))
        errors += 1
        sys.exit(1)
    check("config.json 是合法 JSON", True)

    ai = raw.get("ai", {})
    if not ai:
        check("config.json 包含 ai 配置段", False)
        errors += 1
        sys.exit(1)
    check("config.json 包含 ai 配置段", True)

    # ── 3. Provider ──────────────────────────────────────────
    print("\n3. AI Provider")
    VALID_PROVIDERS = {"anthropic", "openai", "azure", "ali",
                       "gemini", "doubao", "minimax", "deepseek", "ollama"}
    provider = ai.get("provider", "")
    check(f"provider: {provider}", provider in VALID_PROVIDERS,
          f"有效值: {', '.join(sorted(VALID_PROVIDERS))}")
    if provider not in VALID_PROVIDERS:
        errors += 1

    # ── 4. API Key resolution ────────────────────────────────
    print("\n4. API Key 解析")
    api_key_env = ai.get("api_key_env", "")
    check(f"api_key_env: {api_key_env}", bool(api_key_env))
    if not api_key_env:
        errors += 1

    api_key = os.getenv(api_key_env) or os.getenv("LLM_API_KEY")
    if "${" in api_key_env:
        check(f"api_key_env 含未解析变量", False, api_key_env)
        errors += 1
    elif provider == "ollama":
        check(f"${api_key_env} → ollama (免密钥)", True)
    elif api_key:
        masked = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 16 else api_key
        check(f"${api_key_env} → 已解析", True, masked)
    else:
        msg = f"${api_key_env} → 未找到，回退 LLM_API_KEY → {os.getenv('LLM_API_KEY', '未设置')}"
        check(msg, bool(os.getenv("LLM_API_KEY")))
        if not os.getenv("LLM_API_KEY"):
            errors += 1

    # ── 5. Base URL resolution ───────────────────────────────
    print("\n5. API Endpoint")
    PROVIDER_DEFAULTS = {
        "ali": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "deepseek": "https://api.deepseek.com",
        "doubao": "https://ark.cn-beijing.volces.com/api/v3",
        "minimax": "https://api.minimax.io/v1",
        "ollama": "http://localhost:11434/v1",
    }
    env_base = os.getenv("LLM_BASE_URL")
    config_base = ai.get("base_url")
    resolved_base = env_base or config_base or PROVIDER_DEFAULTS.get(provider, "无默认值")
    source = "LLM_BASE_URL" if env_base else ("config.base_url" if config_base else "provider 默认")
    unresolved = "${" in str(resolved_base)
    check(f"base_url: {resolved_base}", bool(resolved_base) and not unresolved,
          f"来源: {source}{'  ⚠ 含未解析的变量引用!' if unresolved else ''}")
    if unresolved:
        errors += 1

    if provider == "azure":
        endpoint_env = ai.get("azure_endpoint_env", "")
        endpoint = os.getenv("LLM_BASE_URL") or os.getenv(endpoint_env)
        check(f"azure_endpoint_env: {endpoint_env}", bool(endpoint_env))
        check(f"Azure endpoint → {'已解析' if endpoint else '未找到'}", bool(endpoint))
        check(f"api_version: {ai.get('api_version', '')}", bool(ai.get("api_version")))
        if not endpoint or not ai.get("api_version"):
            errors += 1

    # ── 6. Model resolution ──────────────────────────────────
    print("\n6. Model")
    env_model = os.getenv("LLM_MODEL")
    config_model = ai.get("model", "")
    resolved_model = env_model or config_model
    source = "LLM_MODEL" if env_model else "config.model"
    check(f"model: {resolved_model}", bool(resolved_model), f"来源: {source}")
    if not resolved_model:
        errors += 1

    # ── 7. Languages ─────────────────────────────────────────
    print("\n7. Languages")
    langs = ai.get("languages", ["en"])
    check(f"languages: {langs}", bool(langs))

    # ── 8. Optional: live API test ───────────────────────────
    print(f"\n{'='*50}")
    if errors == 0 and os.getenv("LLM_API_KEY"):
        print("  全部静态检查通过。执行一次 API 调用确认连通性?")
        print("  (会消耗 ~50 tokens)")
        ans = input("  回车测试, n 跳过: ").strip().lower()
        if ans not in ("n", "no"):
            _live_test(raw, provider, resolved_model, resolved_base, api_key)
        else:
            print("  跳过 API 测试")
    else:
        print(f"  发现 {errors} 个问题，跳过 API 测试")

    # ── Summary ──────────────────────────────────────────────
    print(f"\n{'='*50}")
    if errors == 0:
        print("  ✔  所有配置项校验通过")
    else:
        print(f"  ✘  存在 {errors} 个问题，请根据上方 ✘ 标记修正")
    print(f"{'='*50}\n")
    sys.exit(0 if errors == 0 else 1)


def _live_test(raw: dict, provider: str, model: str, base_url: str, api_key: str):
    """Make a minimal API call to verify connectivity."""
    from src.models import AIConfig
    from src.ai.client import create_ai_client

    config_dict = {
        "provider": provider,
        "model": model,
        "base_url": base_url,
        "api_key_env": "LLM_API_KEY",
        "temperature": 0.3,
        "max_tokens": 128,
        "analysis_concurrency": 1,
        "enrichment_concurrency": 1,
        "languages": ["zh"],
    }
    if provider == "azure":
        config_dict["azure_endpoint_env"] = raw.get("ai", {}).get("azure_endpoint_env")
        config_dict["api_version"] = raw.get("ai", {}).get("api_version")

    ai_config = AIConfig(**config_dict)

    async def test():
        client = create_ai_client(ai_config)
        resp = await client.complete(
            system="Say hello in one word.",
            user="Hello",
        )
        return resp

    try:
        result = asyncio.run(test())
        check("API 连通性测试", True, f"响应: {result.strip()[:60]}")
    except Exception as e:
        check("API 连通性测试", False, str(e)[:100])


if __name__ == "__main__":
    main()
