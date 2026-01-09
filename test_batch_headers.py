import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()

print("=== 测试批量添加header功能 ===")

# 测试数据：用户提供的header字符串
headers_string = """Host: stage2.51tyty.com 
DeviceType: 0 
AppType: 6 
industryType: Education 
DeviceUniqueId: 00000000-42b2-f0d3-0000-000007c52cc7-com.lingshi.inst.klxt-fuxi 
InstId: 6925 
serverId: 1201 
uc: TYTY_DEBUG_CHANNEL 
AppVersion: 5.2.64.210376 
FromAppName: APP 
username: adminqamb 
lan: ch 
Requestuniqueid: 848776_6925_1767751253535_49 
timeZone: GMT+08 
deviceCategory: PAD 
token: 848776:1830740301:b0db752a-2a29-4255-8fa4-bd34f4c1814e:63b14f93b74c63d4890160522da74046:1201v 
Content-Type: application/json"""

# 使用新方法批量添加header
mp.set_headers_from_string(headers_string)

# 打印添加的header
print("\n添加的请求头:")
headers = mp.sessions["default"]["headers"]
for key, value in headers.items():
    print(f"{key}: {value}")

# 测试获取单个header
print("\n测试获取单个header:")
print(f"Host: {headers.get('Host')}")
print(f"token: {headers.get('token')}")
print(f"Content-Type: {headers.get('Content-Type')}")

# 测试在不同会话中使用
print("\n测试在不同会话中使用:")
mp.create_session("new_session")
mp.switch_session("new_session")
mp.set_headers_from_string(headers_string)
new_headers = mp.sessions["new_session"]["headers"]
print(f"新会话中的Host: {new_headers.get('Host')}")

print("\n=== 批量添加header测试成功 ===")
