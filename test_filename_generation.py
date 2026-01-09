import sys
import os
import re

print("=== 测试文件名生成逻辑 ===")

# 模拟send_request中的文件名生成逻辑
def generate_filename(title, filename="response.json"):
    """生成安全的文件名"""
    if filename == "response.json" and title:
        # 替换非字母数字字符为下划线
        safe_title = re.sub(r'[^\w\-\.]', '_', title)
        # 确保文件名以.json结尾
        if not safe_title.endswith('.json'):
            safe_title = f"{safe_title}.json"
        return safe_title
    return filename

# 测试用例
test_cases = [
    # (title, filename, expected)
    ("获取单个任务", "response.json", "获取单个任务.json"),
    ("任务详情.json", "response.json", "任务详情.json"),
    ("获取_任务@测试", "response.json", "获取_任务_测试.json"),
    ("API/测试", "response.json", "API_测试.json"),
    ("测试 空格", "response.json", "测试_空格.json"),
    ("测试123", "response.json", "测试123.json"),
    ("测试", "custom.json", "custom.json"),  # 自定义文件名优先
    ("", "response.json", "response.json"),  # 空标题
]

# 运行测试
for i, (title, filename, expected) in enumerate(test_cases):
    result = generate_filename(title, filename)
    status = "✅" if result == expected else "❌"
    print(f"测试{i+1}: {status} title='{title}', filename='{filename}' -> '{result}' (预期: '{expected}')")
    if result != expected:
        print(f"   测试{i+1}失败")

print("\n=== 所有测试完成 ===")
