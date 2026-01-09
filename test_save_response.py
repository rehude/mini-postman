import sys
import os
import json

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试保存响应JSON到文件功能 ===")

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")

# 测试1: 发送请求并自动保存响应到文件
print("\n测试1: 发送请求并自动保存响应到文件")
try:
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/1", save_to_file=True)
    print(f"状态码: {response.status_code}")
    
    # 验证文件是否存在
    response_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "response", "response.json")
    if os.path.exists(response_file):
        print(f"✅ 文件已创建: {response_file}")
        
        # 读取文件内容并验证
        with open(response_file, "r", encoding="utf-8") as f:
            file_content = json.load(f)
            print(f"✅ 文件内容: {file_content}")
    else:
        print(f"❌ 文件未创建: {response_file}")
except Exception as e:
    print(f"❌ 测试1失败: {e}")

# 测试2: 发送请求并保存到自定义文件名
print("\n测试2: 发送请求并保存到自定义文件名")
try:
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/2", save_to_file=True, filename="todo_2.json")
    print(f"状态码: {response.status_code}")
    
    # 验证文件是否存在
    custom_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "response", "todo_2.json")
    if os.path.exists(custom_file):
        print(f"✅ 自定义文件已创建: {custom_file}")
    else:
        print(f"❌ 自定义文件未创建: {custom_file}")
except Exception as e:
    print(f"❌ 测试2失败: {e}")

# 测试3: 重新请求同一接口，验证文件被覆盖
print("\n测试3: 重新请求同一接口，验证文件被覆盖")
try:
    # 第一次请求
    response1 = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/3")
    mp.save_response_to_file(filename="todo_3.json")
    
    with open(os.path.join("response", "todo_3.json"), "r", encoding="utf-8") as f:
        content1 = json.load(f)
    print(f"第一次请求内容: {content1}")
    
    # 第二次请求不同资源
    response2 = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/4")
    mp.save_response_to_file(filename="todo_3.json")
    
    with open(os.path.join("response", "todo_3.json"), "r", encoding="utf-8") as f:
        content2 = json.load(f)
    print(f"第二次请求内容: {content2}")
    
    if content1 != content2:
        print("✅ 文件已被成功覆盖")
    else:
        print("❌ 文件未被覆盖")
except Exception as e:
    print(f"❌ 测试3失败: {e}")

# 测试4: 手动保存响应到文件
print("\n测试4: 手动保存响应到文件")
try:
    # 发送请求但不自动保存
    response = mp.send_request("GET", "https://jsonplaceholder.typicode.com/todos/5")
    print(f"状态码: {response.status_code}")
    
    # 手动保存
    mp.save_response_to_file(filename="manual_save.json")
    
    # 验证文件是否存在
    manual_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "response", "manual_save.json")
    if os.path.exists(manual_file):
        print(f"✅ 手动保存文件已创建: {manual_file}")
    else:
        print(f"❌ 手动保存文件未创建: {manual_file}")
except Exception as e:
    print(f"❌ 测试4失败: {e}")

print("\n=== 所有测试完成 ===")
