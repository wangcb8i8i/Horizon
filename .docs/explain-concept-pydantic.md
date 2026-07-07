# Pydantic

> Python 运行时数据校验库，用类型注解声明数据结构，自动做类型转换和验证。

## Pydantic Model (BaseModel)

> 声明式数据模型——你写类型注解，它帮你做校验、转换、序列化。

### 本质

用 Python 类型注解定义数据 class，解析时自动验证和转换字段类型。

### 动机

从 API/数据库/配置文件拿到的数据不可信，手写校验代码又重复又容易漏。Pydantic 让你声明「字段是什么类型」，自动处理一切。

### 边界

| | TypedDict | dataclass | Pydantic model |
|--|-----------|-----------|----------------|
| 运行时存在 | ✗ 编译期消失 | ✓ | ✓ |
| 类型校验 | ✗ | ✗ 只存 annotation | ✓ 自动校验+转换 |
| `"123"` 赋给 `int` 字段 | 编译期报类型错 | 运行时当 str | 自动转成 123 |
| JSON 解析 | 手动 | 手动 | `model_validate_json` 一行搞定 |

### 位置

```
Python 数据类生态
  ├── 内置
  │   ├── dict          — 无结构约束
  │   ├── TypedDict     — 编译期约束，零运行时
  │   ├── dataclass     — 有结构的类，无校验
  │   └── NamedTuple    — 不可变结构
  └── 第三方库
       └── Pydantic     — 声明式 + 运行时校验 + JSON 原生支持
```

### 机制

```python
from pydantic import BaseModel

class ContentItem(BaseModel):
    id: str
    title: str
    score: int = 0
    tags: list[str] = []

# 自动类型转换
item = ContentItem(id="1", title="hello", score="5")
item.score  # 5 (int) — 自动从 "5" 转成 int

# JSON 直接解析
item = ContentItem.model_validate_json('{"id":"1","title":"hello","score":"5"}')

# 双方向序列化
item.model_dump()          # → dict
item.model_dump_json()     # → JSON str

# 校验失败
ContentItem(id=1, title="hello")
# id=1 (int) → 自动转为 "1" (str)，不会报错
# 但如果类型完全不可转换才抛 ValidationError
```

### 关联

- `TypedDict` — 同是声明结构，但 Pydantic 有运行时校验，TypedDict 零开销。
- `@dataclass` — 同是生成 class，但 Pydantic 在 `__init__` 里插入了校验逻辑。
- `marshmallow` / `attrs` — 同领域竞品。
