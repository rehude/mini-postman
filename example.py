from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 示例1: 基本GET请求 ===")
# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")

# 发送GET请求
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")

# 查看响应状态码
print(f"状态码: {response.status_code}")

# 查看响应文本
print("响应文本:")
print(mp.get_response_text())

# 查看响应JSON
print("响应JSON:")
print(mp.get_response_json())

# 提取字段
mp.extract_field("userId", "user_id")
user_id = mp.get_extracted_field("user_id")
print(f"提取的userId: {user_id}")

print("\n=== 示例2: 使用提取的字段发送POST请求 ===")
# 创建新会话，复制自默认会话
mp.create_session("post_session", copy_from="default")

# 切换到新会话
mp.switch_session("post_session")

# 设置JSON数据
mp.set_json({"title": "Test Post", "completed": False})

# 使用提取的字段更新JSON数据
mp.update_from_extracted("json", "userId", "user_id")

# 发送POST请求
response = mp.send_request("POST", "https://jsonplaceholder.typicode.com/todos")
print(f"状态码: {response.status_code}")
print("响应JSON:")
print(mp.get_response_json())

print("\n=== 示例3: 会话管理 ===")
# 列出所有会话
print(f"所有会话: {mp.list_sessions()}")

# 切换回默认会话
mp.switch_session("default")

# 查看默认会话的响应
print("默认会话的响应:")
print(mp.get_response_json())

print("\n=== 示例4: 设置查询参数 ===")
# 设置查询参数
mp.set_param("userId", user_id)

# 发送带查询参数的GET请求
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos")
print(f"状态码: {response.status_code}")
print(f"响应条数: {len(mp.get_response_json())}")

print("\n=== 示例5: 复制会话并修改参数 ===")
# 复制会话
mp.create_session("copy_session", copy_from="default")
mp.switch_session("copy_session")

# 修改查询参数
mp.set_param("userId", 2)

# 发送请求
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos")
print(f"状态码: {response.status_code}")
print(f"响应条数: {len(mp.get_response_json())}")
