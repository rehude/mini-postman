import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试真实HTTP请求 ===")
print("使用 https://jsonplaceholder.typicode.com API 进行测试")

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")
mp.set_header("Content-Type", "application/json")

# 测试1: GET请求获取单个资源
print("\n测试1: GET请求获取单个资源")
try:
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")
    print(f"状态码: {response.status_code}")
    print(f"响应JSON: {mp.get_response_json()}")
    print("✅ GET请求测试成功")
except Exception as e:
    print(f"❌ GET请求测试失败: {e}")

# 测试2: 提取字段并使用
print("\n测试2: 提取字段并使用")
try:
    # 从之前的响应中提取userId
    mp.extract_field("userId", "user_id")
    user_id = mp.get_extracted_field("user_id")
    print(f"提取的userId: {user_id}")
    
    # 使用提取的userId发送GET请求
    mp.set_param("userId", user_id)
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos")
    print(f"状态码: {response.status_code}")
    response_json = mp.get_response_json()
    print(f"返回的任务数量: {len(response_json)}")
    print("✅ 字段提取和使用测试成功")
except Exception as e:
    print(f"❌ 字段提取和使用测试失败: {e}")

# 测试3: POST请求创建资源
print("\n测试3: POST请求创建资源")
try:
    # 创建新会话用于POST请求
    mp.create_session("post_session")
    mp.switch_session("post_session")
    
    # 设置请求头
    mp.set_header("User-Agent", "MiniPostman/1.0")
    mp.set_header("Content-Type", "application/json")
    
    # 设置JSON数据
    post_data = {
        "title": "测试任务",
        "body": "这是一个测试任务的内容",
        "userId": 1
    }
    mp.set_json(post_data)
    
    # 发送POST请求
    response = mp.send_request("POST", "https://jsonplaceholder.typicode.com/posts")
    print(f"状态码: {response.status_code}")
    print(f"响应JSON: {mp.get_response_json()}")
    print("✅ POST请求测试成功")
except Exception as e:
    print(f"❌ POST请求测试失败: {e}")

# 测试4: PUT请求更新资源
print("\n测试4: PUT请求更新资源")
try:
    # 创建新会话用于PUT请求
    mp.create_session("put_session")
    mp.switch_session("put_session")
    
    # 设置请求头
    mp.set_header("User-Agent", "MiniPostman/1.0")
    mp.set_header("Content-Type", "application/json")
    
    # 设置JSON数据
    put_data = {
        "id": 1,
        "title": "更新后的测试任务",
        "body": "这是更新后的测试任务内容",
        "userId": 1
    }
    mp.set_json(put_data)
    
    # 发送PUT请求
    response = mp.send_request("PUT", "https://jsonplaceholder.typicode.com/posts/1")
    print(f"状态码: {response.status_code}")
    print(f"响应JSON: {mp.get_response_json()}")
    print("✅ PUT请求测试成功")
except Exception as e:
    print(f"❌ PUT请求测试失败: {e}")

# 测试5: DELETE请求删除资源
print("\n测试5: DELETE请求删除资源")
try:
    # 创建新会话用于DELETE请求
    mp.create_session("delete_session")
    mp.switch_session("delete_session")
    
    # 设置请求头
    mp.set_header("User-Agent", "MiniPostman/1.0")
    
    # 发送DELETE请求
    response = mp.send_request("DELETE", "https://jsonplaceholder.typicode.com/posts/1")
    print(f"状态码: {response.status_code}")
    print(f"响应JSON: {mp.get_response_json()}")
    print("✅ DELETE请求测试成功")
except Exception as e:
    print(f"❌ DELETE请求测试失败: {e}")

print("\n=== 所有测试完成 ===")
