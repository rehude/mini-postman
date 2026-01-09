import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mini_postman import MiniPostman

# 创建测试用的模拟响应类
class MockResponse:
    def __init__(self, json_data):
        self._json_data = json_data
    
    def json(self):
        return self._json_data
    
    @property
    def text(self):
        import json
        return json.dumps(self._json_data)

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试extract_field方法（支持数组索引） ===")

# 测试1: 正常数组提取
print("\n测试1: 正常数组提取")
try:
    # 设置模拟响应，data是一个包含对象的数组
    mock_data = {
        "data": [
            {"id": 1, "inst": {"code": "TEST001"}},
            {"id": 2, "inst": {"code": "TEST002"}}
        ]
    }
    mp.sessions["default"]["response"] = MockResponse(mock_data)
    
    # 提取数组中的字段
    mp.extract_field("data[0].inst.code", "inst_code")
    inst_code = mp.get_extracted_field("inst_code")
    print(f"✅ 提取成功: data[0].inst.code = {inst_code}")
    
    # 提取第二个元素
    mp.extract_field("data[1].id", "second_id")
    second_id = mp.get_extracted_field("second_id")
    print(f"✅ 提取成功: data[1].id = {second_id}")
except Exception as e:
    print(f"❌ 测试1失败: {e}")

# 测试2: 空数组处理
print("\n测试2: 空数组处理")
try:
    # 设置模拟响应，data是一个空数组
    mock_data = {"data": []}
    mp.sessions["default"]["response"] = MockResponse(mock_data)
    
    # 尝试从空数组提取字段
    mp.extract_field("data[0].inst.code", "inst_code")
    print("❌ 测试2失败: 应该抛出异常")
except ValueError as e:
    print(f"✅ 测试2成功: 空数组正确抛出异常 - {e}")

# 测试3: 索引越界处理
print("\n测试3: 索引越界处理")
try:
    # 设置模拟响应，data只有一个元素
    mock_data = {
        "data": [{"id": 1, "inst": {"code": "TEST001"}}]
    }
    mp.sessions["default"]["response"] = MockResponse(mock_data)
    
    # 尝试访问不存在的索引
    mp.extract_field("data[5].id", "invalid_id")
    print("❌ 测试3失败: 应该抛出异常")
except ValueError as e:
    print(f"✅ 测试3成功: 索引越界正确抛出异常 - {e}")

# 测试4: 多级嵌套数组
print("\n测试4: 多级嵌套数组")
try:
    # 设置模拟响应，包含多级嵌套数组
    mock_data = {
        "results": [
            {
                "items": [
                    {"name": "item1", "value": 100},
                    {"name": "item2", "value": 200}
                ]
            }
        ]
    }
    mp.sessions["default"]["response"] = MockResponse(mock_data)
    
    # 提取多级嵌套字段
    mp.extract_field("results[0].items[1].value", "nested_value")
    nested_value = mp.get_extracted_field("nested_value")
    print(f"✅ 测试4成功: results[0].items[1].value = {nested_value}")
except Exception as e:
    print(f"❌ 测试4失败: {e}")

# 测试5: 普通字段提取（确保兼容原有功能）
print("\n测试5: 普通字段提取（兼容原有功能）")
try:
    # 设置模拟响应，包含普通嵌套字段
    mock_data = {
        "user": {
            "id": 123,
            "name": "test_user",
            "profile": {
                "email": "test@example.com"
            }
        }
    }
    mp.sessions["default"]["response"] = MockResponse(mock_data)
    
    # 提取普通嵌套字段
    mp.extract_field("user.profile.email", "user_email")
    user_email = mp.get_extracted_field("user_email")
    print(f"✅ 测试5成功: user.profile.email = {user_email}")
except Exception as e:
    print(f"❌ 测试5失败: {e}")

print("\n=== 所有测试完成 ===")
