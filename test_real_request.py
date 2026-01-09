from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试真正的HTTP请求 ===")

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")
mp.set_header("Content-Type", "application/json")

# 发送GET请求到JSONPlaceholder API
print("发送GET请求到 https://jsonplaceholder.typicode.com/todos/1")
try:
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")
    
    # 查看响应状态码
    print(f"状态码: {response.status_code}")
    
    # 查看响应文本
    print("响应文本:")
    print(mp.get_response_text())
    
    # 查看响应JSON
    print("响应JSON:")
    response_json = mp.get_response_json()
    print(response_json)
    
    # 提取字段
    mp.extract_field("userId", "user_id")
    user_id = mp.get_extracted_field("user_id")
    print(f"提取的userId: {user_id}")
    
    # 使用提取的字段发送另一个请求
    print(f"\n使用提取的userId {user_id} 发送GET请求")
    mp.set_param("userId", user_id)
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos")
    
    print(f"状态码: {response.status_code}")
    response_json = mp.get_response_json()
    print(f"返回的任务数量: {len(response_json)}")
    print("前3个任务:")
    for todo in response_json[:3]:
        print(f"  - {todo['title']} (完成: {todo['completed']})")
    
    print("\n=== HTTP请求测试成功 ===")
except Exception as e:
    print(f"\n=== HTTP请求测试失败 ===")
    print(f"错误信息: {e}")
    print("请确保已安装requests库: py -m pip install requests")
