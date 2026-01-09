from mini_postman import MiniPostman

# 创建实例
mp = MiniPostman()

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")

# 发送GET请求
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")

# 查看响应
print(f"状态码: {response.status_code}")
print(f"响应JSON: {mp.get_response_json()}")

# 提取字段
mp.extract_field("userId", "user_id")
user_id = mp.get_extracted_field("user_id")

# 使用提取的字段发送另一个请求
mp.set_param("userId", user_id)
response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos")