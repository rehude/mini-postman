import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试使用title作为文件名 ===")

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")

# 测试1: 使用title作为文件名，包含特殊字符
print("\n测试1: 使用title作为文件名，包含特殊字符")
try:
    response = mp.send_request(
        "GET", 
        "https://jsonplaceholder.typicode.com/todos/1",
        title="获取_单个任务@测试"
    )
    print(f"✅ 请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 测试1失败: {e}")

# 测试2: 使用title作为文件名，已包含.json后缀
print("\n测试2: 使用title作为文件名，已包含.json后缀")
try:
    response = mp.send_request(
        "GET", 
        "https://jsonplaceholder.typicode.com/todos/2",
        title="任务详情.json"
    )
    print(f"✅ 请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 测试2失败: {e}")

# 测试3: 自定义文件名优先
print("\n测试3: 自定义文件名优先")
try:
    response = mp.send_request(
        "GET", 
        "https://jsonplaceholder.typicode.com/todos/3",
        title="应该被忽略的标题",
        filename="custom_name.json"
    )
    print(f"✅ 请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 测试3失败: {e}")

# 测试4: 验证文件是否创建成功
print("\n测试4: 验证文件是否创建成功")
try:
    from datetime import datetime
    today = datetime.now().strftime("%Y.%m.%d")
    response_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "response", today)
    
    if os.path.exists(response_dir):
        files = os.listdir(response_dir)
        print(f"✅ 日期目录: {response_dir}")
        print(f"✅ 目录中的文件: {files}")
        
        # 验证预期的文件是否存在
        expected_files = [
            "获取_单个任务_测试.json",  # 特殊字符被替换
            "任务详情.json",  # 已包含.json后缀
            "custom_name.json"  # 自定义文件名
        ]
        
        for file in expected_files:
            if file in files:
                print(f"✅ 预期文件已创建: {file}")
            else:
                print(f"❌ 预期文件未创建: {file}")
                print(f"   当前目录文件: {files}")
except Exception as e:
    print(f"❌ 测试4失败: {e}")

print("\n=== 所有测试完成 ===")
