import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试更新后的功能 ===")

# 设置请求头
mp.set_header("User-Agent", "MiniPostman/1.0")

# 测试1: 发送请求，验证接口标题打印和默认保存
print("\n测试1: 发送请求，验证接口标题打印和默认保存")
try:
    response = mp.send_request(
        "GET", 
        "https://jsonplaceholder.typicode.com/todos/1",
        title="获取单个任务"
    )
    print(f"✅ 请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 测试1失败: {e}")

# 测试2: 提取字段，验证直接返回值和打印
print("\n测试2: 提取字段，验证直接返回值和打印")
try:
    # 提取字段并获取返回值
    user_id = mp.extract_field("userId", "user_id")
    print(f"✅ 提取的userId值: {user_id} (类型: {type(user_id).__name__})")
    
    # 再次提取，验证返回值
    title = mp.extract_field("title", "task_title")
    print(f"✅ 提取的title值: {title} (类型: {type(title).__name__})")
except Exception as e:
    print(f"❌ 测试2失败: {e}")

# 测试3: 发送请求，自定义文件名
print("\n测试3: 发送请求，自定义文件名")
try:
    response = mp.send_request(
        "GET", 
        "https://jsonplaceholder.typicode.com/todos/2",
        title="获取第二个任务",
        filename="todo_2.json"
    )
    print(f"✅ 请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 测试3失败: {e}")

# 测试4: 发送请求，禁用保存到文件
print("\n测试4: 发送请求，禁用保存到文件")
try:
    response = mp.send_request(
        "GET", 
        "https://jsonplaceholder.typicode.com/todos/3",
        title="获取第三个任务",
        save_to_file=False
    )
    print(f"✅ 请求成功，状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 测试4失败: {e}")

# 测试5: 验证文件保存路径（检查目录结构）
print("\n测试5: 验证文件保存路径")
try:
    from datetime import datetime
    today = datetime.now().strftime("%Y.%m.%d")
    response_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "response", today)
    
    if os.path.exists(response_dir):
        print(f"✅ 日期目录已创建: {response_dir}")
        
        # 列出目录中的文件
        files = os.listdir(response_dir)
        print(f"✅ 目录中的文件: {files}")
        
        # 检查是否包含我们保存的文件
        expected_files = ["response.json", "todo_2.json"]
        for file in expected_files:
            if file in files:
                print(f"✅ 文件已保存: {file}")
            else:
                print(f"❌ 文件未保存: {file}")
    else:
        print(f"❌ 日期目录未创建: {response_dir}")
except Exception as e:
    print(f"❌ 测试5失败: {e}")

print("\n=== 所有测试完成 ===")
