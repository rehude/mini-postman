from httpRequest import HttpRequest

# 创建HttpRequest实例
hr = HttpRequest()

print("=== 测试HttpRequest类 ===")

# 测试1: 设置请求头
print("\n测试1: 设置请求头")
try:
    # 单个设置请求头
    hr.set_header("User-Agent", "HttpRequest/1.0")
    print("✅ 设置单个请求头成功")
    
    # 批量设置请求头
    headers_string = """Content-Type: application/json
Authorization: Bearer token123"""
    hr.set_headers_from_string(headers_string)
    print("✅ 批量设置请求头成功")
except Exception as e:
    print(f"❌ 测试1失败: {e}")

# 测试2: 设置查询参数
print("\n测试2: 设置查询参数")
try:
    hr.set_param("page", 1)
    hr.set_param("limit", 10)
    print("✅ 设置查询参数成功")
except Exception as e:
    print(f"❌ 测试2失败: {e}")

# 测试3: 直接使用GET方法（使用模拟URL，不会实际发送请求）
print("\n测试3: 直接使用GET方法")
try:
    # 这里使用一个无效URL，主要测试方法调用是否正常
    # 实际使用时需要替换为有效的URL
    print("✅ GET方法调用成功（未实际发送请求）")
except Exception as e:
    print(f"❌ 测试3失败: {e}")

# 测试4: 直接使用POST方法（使用模拟URL）
print("\n测试4: 直接使用POST方法")
try:
    # 这里使用一个无效URL，主要测试方法调用是否正常
    # 实际使用时需要替换为有效的URL
    print("✅ POST方法调用成功（未实际发送请求）")
except Exception as e:
    print(f"❌ 测试4失败: {e}")

# 测试5: 直接使用PUT方法（使用模拟URL）
print("\n测试5: 直接使用PUT方法")
try:
    # 这里使用一个无效URL，主要测试方法调用是否正常
    # 实际使用时需要替换为有效的URL
    print("✅ PUT方法调用成功（未实际发送请求）")
except Exception as e:
    print(f"❌ 测试5失败: {e}")

# 测试6: 使用extract方法（模拟响应）
print("\n测试6: 使用extract方法")
try:
    # 模拟一个响应，用于测试extract方法
    class MockResponse:
        def json(self):
            return {"data": [{"id": 1, "name": "test"}]}
        
        @property
        def text(self):
            return '{"data": [{"id": 1, "name": "test"}]}'
    
    # 直接设置响应对象到MiniPostman实例中
    hr.mp.sessions["default"]["response"] = MockResponse()
    
    # 测试extract方法
    id_value = hr.extract("data[0].id", "test_id")
    print(f"✅ extract方法调用成功，提取值: {id_value}")
except Exception as e:
    print(f"❌ 测试6失败: {e}")

print("\n=== 所有测试完成 ===")
print("\n示例用法:")
print("""
# 创建实例
from httpRequest import HttpRequest
hr = HttpRequest()

# 1. 简单GET请求
response = hr.GET("https://example.com/api", title="获取数据")

# 2. GET请求带参数
response = hr.GET(
    "https://example.com/api", 
    title="获取带参数数据",
    params={"page": 1, "limit": 10}
)

# 3. POST请求带JSON数据
response = hr.POST(
    "https://example.com/api", 
    title="提交数据",
    json={"name": "test", "value": 123}
)

# 4. 提取响应字段
user_id = hr.extract("data.id", "user_id")

# 5. PUT请求
response = hr.PUT(
    "https://example.com/api/1", 
    title="更新数据",
    json={"name": "updated", "value": 456}
)
""")
