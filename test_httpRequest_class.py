from httpRequest import HttpRequest

# 创建HttpRequest实例
def test_httpRequest_class():
    print("=== 测试 HttpRequest 类 ===")
    
    # 创建实例
    hr = HttpRequest()
    
    # 测试1: 批量设置请求头
    print("\n1. 测试批量设置请求头...")
    headers_string = """Host: jsonplaceholder.typicode.com
User-Agent: MiniPostman/1.0
Content-Type: application/json"""
    hr.set_headers_from_string(headers_string)
    print("✅ 请求头设置完成")
    
    # 测试2: 发送GET请求
    print("\n2. 测试发送GET请求...")
    response = hr.GET("https://jsonplaceholder.typicode.com/todos/1", title="测试GET请求")
    print(f"✅ GET请求成功，状态码: {response.status_code}")
    
    # 测试3: 提取字段
    print("\n3. 测试提取字段...")
    user_id = hr.extract("userId", "user_id")
    print(f"✅ 提取字段成功，userId: {user_id}")
    
    # 测试4: 发送POST请求
    print("\n4. 测试发送POST请求...")
    post_data = {
        "title": "Test Task",
        "completed": False,
        "userId": user_id
    }
    response = hr.POST(
        "https://jsonplaceholder.typicode.com/todos",
        title="测试POST请求",
        json=post_data
    )
    print(f"✅ POST请求成功，状态码: {response.status_code}")
    
    # 测试5: 发送PUT请求
    print("\n5. 测试发送PUT请求...")
    put_data = {
        "title": "Updated Task",
        "completed": True,
        "userId": user_id
    }
    response = hr.PUT(
        "https://jsonplaceholder.typicode.com/todos/1",
        title="测试PUT请求",
        json=put_data
    )
    print(f"✅ PUT请求成功，状态码: {response.status_code}")
    
    print("\n=== HttpRequest 类测试完成 ===")

if __name__ == "__main__":
    test_httpRequest_class()
