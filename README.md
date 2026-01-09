# MiniPostman

一个轻量级、高性能的Python HTTP请求工具，比Postman更快、更省内存。

## 功能特性

✅ **自定义HTTP请求头** - 灵活设置各种请求头
✅ **清楚查看HTTP响应体** - 支持JSON和文本格式
✅ **响应字段提取** - 可以将响应中的字段提取出来给下一个请求使用，支持数组索引
✅ **高性能** - 比Postman更快、更省内存
✅ **会话管理** - 支持创建、复制、切换会话，方便管理不同的请求配置
✅ **参数复用** - 支持随时复制、修改参数
✅ **批量请求头** - 从字符串批量设置请求头
✅ **URL自动修复** - 自动添加协议前缀
✅ **SSL验证控制** - 支持开启/关闭SSL验证
✅ **代理设置** - 支持配置HTTP代理
✅ **按日期分类保存** - 自动将请求和响应保存到按日期分类的文件夹
✅ **标题作为文件名** - 自动使用请求标题生成文件名
✅ **自动保存请求** - 自动保存请求信息到文件
✅ **自动保存响应** - 自动保存响应到文件

## 安装

1. 确保已安装Python 3.6+
2. 安装依赖：
```bash
pip install requests
```
3. 下载或克隆本项目

## 快速开始

### 基本使用

```python
from mini_postman import MiniPostman

# 创建实例
mp = MiniPostman()

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")

# 发送GET请求
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")

# 发送请求后会自动打印响应信息
# 无需手动打印，代码会自动显示状态码、请求URL等信息

# 提取字段，直接返回提取的值
user_id = mp.extract_field("userId", "user_id")
print(f"提取的userId: {user_id}")

# 支持数组索引提取，直接返回值
first_id = mp.extract_field("[0].id", "first_id", session="default")
print(f"第一个元素的id: {first_id}")

# 发送带标题、SSL验证和代理的请求
response = mp.send_request(
    "GET", 
    "https://jsonplaceholder.typicode.com/todos",
    title="获取任务列表",
    verify=True,
    proxies={"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"}
)

# URL自动修复功能
response = mp.send_request("GET", "jsonplaceholder.typicode.com/todos/1")
```

### 会话管理

```python
# 创建新会话，复制自默认会话
mp.create_session("new_session", copy_from="default")

# 切换到新会话
mp.switch_session("new_session")

# 列出所有会话
print(mp.list_sessions())
```

### 使用提取的字段

```python
# 使用提取的字段更新请求参数
mp.update_from_extracted("json", "userId", "user_id")

# 发送POST请求
response = mp.send_request("POST", "https://jsonplaceholder.typicode.com/todos")
```

### HttpRequest 类使用示例

```python
from httpRequest import HttpRequest

# 创建HttpRequest实例
hr = HttpRequest()

# 批量设置请求头
headers_string = """Host: jsonplaceholder.typicode.com
User-Agent: MiniPostman/1.0
Content-Type: application/json"""
hr.set_headers_from_string(headers_string)

# 发送GET请求
response = hr.GET("https://jsonplaceholder.typicode.com/todos/1", title="获取任务详情")

# 提取字段
user_id = hr.extract("userId", "user_id")
print(f"提取的userId: {user_id}")

# 发送POST请求，带JSON数据
response = hr.POST(
    "https://jsonplaceholder.typicode.com/todos",
    title="创建新任务",
    json={"title": "Test Task", "completed": False, "userId": user_id}
)

# 发送PUT请求
response = hr.PUT(
    "https://jsonplaceholder.typicode.com/todos/1",
    title="更新任务",
    json={"title": "Updated Task", "completed": True}
)
```

## API参考

### HttpRequest 类

`HttpRequest` 是对 `MiniPostman` 的封装，提供了更简洁的API来发送HTTP请求。

#### 初始化
```python
from httpRequest import HttpRequest

# 创建HttpRequest实例
hr = HttpRequest()
```

#### 主要方法

##### `GET(url, title="GET请求", **kwargs)`
发送GET请求
- `url`: 请求URL
- `title`: 接口标题，用于生成文件名
- `**kwargs`: 可选参数
  - `session`: 会话名称
  - `headers`: 请求头字典
  - `params`: 查询参数字典
  - `save_to_file`: 是否保存响应到文件（默认True）
  - `verify`: 是否验证SSL证书（默认False）
  - `proxies`: 代理设置字典
- 返回: 响应对象

##### `POST(url, title="POST请求", **kwargs)`
发送POST请求
- `url`: 请求URL
- `title`: 接口标题，用于生成文件名
- `**kwargs`: 可选参数
  - `session`: 会话名称
  - `headers`: 请求头字典
  - `data`: 表单数据字典
  - `json`: JSON数据字典
  - `save_to_file`: 是否保存响应到文件（默认True）
  - `verify`: 是否验证SSL证书（默认False）
- 返回: 响应对象

##### `PUT(url, title="PUT请求", **kwargs)`
发送PUT请求
- `url`: 请求URL
- `title`: 接口标题，用于生成文件名
- `**kwargs`: 可选参数
  - `session`: 会话名称
  - `headers`: 请求头字典
  - `data`: 表单数据字典
  - `json`: JSON数据字典
  - `save_to_file`: 是否保存响应到文件（默认True）
  - `verify`: 是否验证SSL证书（默认False）
- 返回: 响应对象

##### `extract(field_path, alias, session=None)`
提取响应字段
- `field_path`: 字段路径，如 "data[0].id"
- `alias`: 字段别名
- `session`: 会话名称
- 返回: 提取的字段值

##### `set_headers_from_string(headers_string, session=None)`
从字符串批量设置请求头
- `headers_string`: 请求头字符串，格式为每行一个 "Key: Value"
- `session`: 会话名称

### 核心方法

#### `set_header(key, value, session=None)`
设置请求头
- `key`: 请求头键
- `value`: 请求头值
- `session`: 会话名称，默认为当前会话

#### `set_headers_from_string(headers_string, session=None)`
从字符串批量设置请求头，格式为每行一个header: Key: Value
- `headers_string`: 包含多个请求头的字符串，每行一个键值对
- `session`: 会话名称，默认为当前会话

#### `set_param(key, value, session=None)`
设置查询参数
- `key`: 参数键
- `value`: 参数值
- `session`: 会话名称，默认为当前会话

#### `set_data(key, value, session=None)`
设置表单数据
- `key`: 数据键
- `value`: 数据值
- `session`: 会话名称，默认为当前会话

#### `set_json(data, session=None)`
设置JSON数据
- `data`: JSON数据字典
- `session`: 会话名称，默认为当前会话

#### `send_request(method, url, session=None, title="", save_to_file=True, filename="response.json", verify=False, proxies=None, **kwargs)`
发送HTTP请求
- `method`: 请求方法（GET, POST, PUT, DELETE等）
- `url`: 请求URL
- `session`: 会话名称，默认为当前会话
- `title`: 请求标题，用于标识请求，会自动作为文件名
- `save_to_file`: 是否自动保存响应到文件，默认为True
- `filename`: 保存响应的文件名，默认为"response.json"
- `verify`: 是否验证SSL证书，默认为False
- `proxies`: 代理设置字典，默认为None
- `**kwargs`: 其他请求参数
- 返回: requests.Response对象

#### `get_response_text(session=None)`
获取响应文本
- `session`: 会话名称，默认为当前会话
- 返回: 响应文本字符串

#### `get_response_json(session=None)`
获取响应JSON
- `session`: 会话名称，默认为当前会话
- 返回: 响应JSON字典

#### `extract_field(field_path, alias, session=None)`
从响应中提取字段，支持嵌套路径和数组索引，并直接返回提取的值
- `field_path`: 字段路径，支持嵌套路径和数组索引，如 "data.user.id" 或 "data[0].inst.code"
- `alias`: 提取字段的别名，用于后续引用
- `session`: 会话名称，默认为当前会话
- 返回: 提取的字段值

#### `get_extracted_field(alias, session=None)`
获取之前提取的字段值（可选，因为extract_field会直接返回值）
- `alias`: 提取字段的别名
- `session`: 会话名称，默认为当前会话
- 返回: 提取的字段值

#### `update_from_extracted(target, key, alias, session=None)`
使用提取的字段更新请求参数
- `target`: 目标类型，可选值："header", "param", "data", "json"
- `key`: 目标键
- `alias`: 提取字段的别名
- `session`: 会话名称，默认为当前会话

#### `save_request_to_file(method, url, request_kwargs, title, session=None, filename="request.json")`
保存请求信息到文件
- `method`: 请求方法
- `url`: 请求URL
- `request_kwargs`: 请求参数
- `title`: 请求标题
- `session`: 会话名称，默认为当前会话
- `filename`: 保存请求的文件名，默认为"request.json"

#### `save_response_to_file(method="", url="", request_kwargs={}, title="", session=None, filename="response.json")`
保存响应到文件
- `method`: 请求方法（可选）
- `url`: 请求URL（可选）
- `request_kwargs`: 请求参数（可选）
- `title`: 请求标题，用于生成文件名
- `session`: 会话名称，默认为当前会话
- `filename`: 保存响应的文件名，默认为"response.json"

### 会话管理方法

#### `create_session(name, copy_from=None)`
创建新会话
- `name`: 会话名称
- `copy_from`: 从哪个会话复制，默认为空

#### `switch_session(name)`
切换会话
- `name`: 会话名称

#### `delete_session(name)`
删除会话
- `name`: 会话名称

#### `list_sessions()`
列出所有会话
- 返回: 会话名称列表

#### `clear_session(session=None)`
清空会话数据
- `session`: 会话名称，默认为当前会话

## 示例

查看 `example.py` 文件获取更多使用示例。

## 性能对比

与Postman相比，MiniPostman具有以下优势：

- **启动速度快** - 无需等待大型应用启动
- **内存占用低** - 仅占用Python进程内存，远低于Electron应用
- **响应速度快** - 直接调用Python库，减少中间层开销
- **脚本化** - 支持编写脚本，便于自动化测试和批量请求

## 适用场景

- API开发和测试
- 自动化测试脚本
- 数据抓取和分析
- API集成调试
- 性能测试

## 许可证

MIT License
