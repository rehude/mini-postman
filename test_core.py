class MockResponse:
    """模拟响应对象"""
    def __init__(self, status_code, json_data, text):
        self.status_code = status_code
        self._json_data = json_data
        self._text = text
    
    def json(self):
        return self._json_data
    
    @property
    def text(self):
        return self._text

# 测试核心功能
from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试核心功能 ===")

# 测试1: 设置和获取请求头
print("测试1: 设置和获取请求头")
mp.set_header("User-Agent", "MiniPostman/1.0")
mp.set_header("Content-Type", "application/json")
print(f"请求头: {mp.sessions['default']['headers']}")

# 测试2: 设置和获取参数
print("\n测试2: 设置和获取参数")
mp.set_param("key1", "value1")
mp.set_param("key2", 123)
print(f"查询参数: {mp.sessions['default']['params']}")

# 测试3: 设置和获取JSON数据
print("\n测试3: 设置和获取JSON数据")
mp.set_json({"name": "test", "value": 456})
print(f"JSON数据: {mp.sessions['default']['json']}")

# 测试4: 模拟响应处理
print("\n测试4: 模拟响应处理")
# 手动设置模拟响应
mock_response = MockResponse(200, {"id": 1, "userId": 100, "title": "test"}, '{"id": 1, "userId": 100, "title": "test"}')
mp.sessions['default']['response'] = mock_response

print(f"状态码: {mp.sessions['default']['response'].status_code}")
print(f"响应文本: {mp.get_response_text()}")
print(f"响应JSON: {mp.get_response_json()}")

# 测试5: 字段提取
print("\n测试5: 字段提取")
mp.extract_field("userId", "user_id")
mp.extract_field("id", "item_id")
print(f"提取的字段: {mp.sessions['default']['extracted_fields']}")
print(f"获取提取的userId: {mp.get_extracted_field('user_id')}")

# 测试6: 会话管理
print("\n测试6: 会话管理")
mp.create_session("new_session", copy_from="default")
print(f"所有会话: {mp.list_sessions()}")

# 测试7: 使用提取的字段更新请求
print("\n测试7: 使用提取的字段更新请求")
mp.update_from_extracted("json", "userId", "user_id")
print(f"更新后的JSON数据: {mp.sessions['default']['json']}")

print("\n=== 所有测试完成 ===")
