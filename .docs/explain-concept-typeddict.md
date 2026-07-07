# TypedDict (Python typing)

> `typing` 模块中给字典结构定义精确键名和类型的类型注解工具。

## TypedDict

> 带类型约束的字典——只存在类型检查期，运行时就是一个普通 dict。

### 本质

给字典的键名和值类型做声明。类似接口之于类。

### 动机

普通 `dict` 没有结构约束，IDE 和类型检查器无法发现键名拼写错误或类型不匹配。TypedDict 让字典也有「接口」，且运行时零开销。

### 边界

- TypedDict <u>不是</u> dataclass：无属性访问（`d.name` 不行）、无方法、无运行时校验
- 只存在于类型检查阶段，运行时就是一个普通 `dict`
- 与 dataclass / NamedTuple 同级，区别在于 TypedDict 不生成新类

### 位置

```
typing 模块
  ├── 基础类型 (str, int, ...)
  ├── 泛型 (Generic, TypeVar)
  └── 结构类型
       ├── Protocol           — 描述"有某方法/属性"的接口
       └── TypedDict          — 描述"有某键值对"的字典结构
```

### 用法

```python
# class 语法（支持继承、docstring）
class ProgressHooks(TypedDict, total=False):
    on_plugin_start: str
    on_item: int

# 函数调用语法
ProgressHooks = TypedDict("ProgressHooks", {
    "on_plugin_start": str,
    "on_item": int,
}, total=False)
```

### 关联

- `@dataclass` — 也有名字字段，但生成真正的类、有 `__init__`、可加方法。开销比 TypedDict 大。
- `NamedTuple` — 元组带名字，不可变，也比普通 dict 重。
- `Protocol` — 描述方法结构而非数据结构的接口。
