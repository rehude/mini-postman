# MiniPostman 启动说明

## 工具简介

MiniPostman 是一个轻量级的 Python HTTP 请求工具，具有以下特点：
- ✅ 自定义 HTTP 请求头
- ✅ 清楚查看 HTTP 响应体（JSON / text）
- ✅ 能把响应里的字段，拿出来给下一个请求用，支持数组索引
- ✅ 比 Postman 快、不吃内存
- ✅ 可以随时复制、改参数
- ✅ 支持批量添加请求头
- ✅ URL 自动修复（自动添加协议前缀）
- ✅ 支持 SSL 验证开关
- ✅ 支持代理设置
- ✅ 自动保存请求和响应到按日期分类的文件夹
- ✅ 支持标题作为文件名
- ✅ 自动生成请求和响应文件名称

## 环境要求

- Python 3.6 或更高版本

## 快速开始

### 1. 测试核心功能

首先，我们可以运行测试脚本，验证工具的核心功能是否正常工作：

```bash
# 在项目根目录下执行
py test_core.py
```

如果看到类似以下输出，说明测试通过：
```
=== 测试核心功能 ===
测试1: 设置和获取请求头
请求头: {'User-Agent': 'MiniPostman/1.0', 'Content-Type': 'application/json'}
...
=== 所有测试完成 ===
```

### 2. 安装依赖（用于实际发送HTTP请求）

要发送真正的 HTTP 请求，必须安装 `requests` 库：

```bash
py -m pip install requests
```

### 2.1 验证requests库安装

创建一个简单的验证脚本 `check_requests.py`：

```python
try:
    import requests
    print("✅ requests库安装成功！")
    print(f"   版本: {requests.__version__}")
except ImportError:
    print("❌ requests库未安装！")
    print("   请运行: py -m pip install requests")
```

运行验证脚本：
```bash
py check_requests.py
```

### 3. 运行示例脚本

查看工具的实际使用示例：

```bash
# 在项目根目录下执行
py example.py
```

### 4. 基本使用 - 发送真正的HTTP请求

创建一个脚本 `my_real_request.py`，内容如下：

```python
from mini_postman import MiniPostman

# 创建实例
mp = MiniPostman()

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")
mp.set_header("Content-Type", "application/json")

# 发送GET请求到JSONPlaceholder API
print("发送GET请求...")
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")

# 查看响应
print(f"状态码: {response.status_code}")
print(f"响应JSON: {mp.get_response_json()}")

# 提取字段
mp.extract_field("userId", "user_id")
user_id = mp.get_extracted_field("user_id")
print(f"提取的userId: {user_id}")

# 使用提取的字段发送另一个请求
print(f"\n使用提取的userId {user_id} 发送GET请求...")
mp.set_param("userId", user_id)
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos")

print(f"状态码: {response.status_code}")
response_json = mp.get_response_json()
print(f"返回的任务数量: {len(response_json)}")
```

运行脚本：
```bash
py my_real_request.py
```

### 5. 运行真实请求测试脚本

我们提供了一个专门的测试脚本，用于验证真实HTTP请求功能：

```bash
py test_real_request.py
```

## 核心功能说明

### 1. 会话管理

```python
# 创建新会话，复制自默认会话
mp.create_session("new_session", copy_from="default")

# 切换到新会话
mp.switch_session("new_session")

# 列出所有会话
print(mp.list_sessions())
```

### 2. 字段提取与复用

```python
# 从响应中提取字段
mp.extract_field("userId", "user_id")

# 获取提取的字段值
user_id = mp.get_extracted_field("user_id")

# 使用提取的字段更新请求参数
mp.update_from_extracted("json", "userId", "user_id")
```

## 注意事项

1. 测试脚本 `test_core.py` 不依赖 `requests` 库，可以直接运行
2. 实际发送 HTTP 请求需要安装 `requests` 库
3. 工具支持多种请求方法：GET、POST、PUT、DELETE 等
4. 每个会话独立管理自己的请求配置和响应

## 进阶使用

查看 `README.md` 文件获取完整的 API 文档和更多使用示例。
