import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()
# http://stage2.51tyty.com/resource/services/rest/qrcode/WechatLogin/CreateKey/sjjjk11112138714

# 设置请求头
header_string = """
Host: stage2.51tyty.com
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
timeZone: GMT+08
deviceCategory: PAD
token: 848776:1830740301:b0db752a-2a29-4255-8fa4-bd34f4c1814e:63b14f93b74c63d4890160522da74046:1201v
Content-Type: application/json
"""


mp.set_headers_from_string(header_string)

# 测试1: GET请求获取单个资源
print("\n测试: PUT 请求用户名授权登录 小程序")
try:
     # 创建新会话用于PUT请求
    mp.create_session("put_session")
    mp.switch_session("put_session")
    
    # 设置请求头
    mp.set_headers_from_string(header_string,session="put_session")

    
    # 设置JSON数据
    # put_data = {
    #     "id": 1,
    #     "title": "更新后的测试任务",
    #     "body": "这是更新后的测试任务内容",
    #     "userId": 1
    # }
    # mp.set_json(put_data)
    userName = '18870704048'
    # 发送PUT请求
    response = mp.send_request("PUT", f"http://stage2.51tyty.com/resource/services/rest/qrcode/WechatLogin/CreateKey/{userName}",save_to_file=True,filename="1微信Sign生成.json")
    print(f"状态码: {response.status_code}")
    print(f"响应JSON: {mp.get_response_json()}")
    print("1✅ PUT请求测试成功")

        # 从之前的响应中提取userId
    mp.extract_field("qrCode.qrCodeKey", "qrCodeKey")
    sign = qrCodeKey = mp.get_extracted_field("qrCodeKey")
    print(f"提取的qrCodeKey: {qrCodeKey}")
    
    # 使用提取的userId发送GET请求
    mp.set_param("userId", qrCodeKey)
    # 设置请求头
    mp.set_headers_from_string(header_string,session="put_session")



    
    response = mp.send_request("GET", f"http://stage2.51tyty.com/center/services/rest/user/authorizationRegister/V2/{userName}/{qrCodeKey}",save_to_file=True,filename="2机构列表.json")
    #response = mp.send_request("GET", f"http://127.0.0.1:8115/center/services/rest/user/authorizationRegister/V2/{userName}/{qrCodeKey}",save_to_file=True,filename="2机构列表.json")
    print(f"状态码: {response.status_code}")
    #print(f"响应JSON: {mp.get_response_json()}")
    print("2✅ GET 机构列表请求测试成功")


    # 获取必要的请求头参数
    
    mp.extract_field("data[0].inst.code", "IG")
    IG = mp.get_extracted_field("IG")
    print(f"提取的IG: {IG}")

    mp.set_header("IG", f"{IG}")

    mp.extract_field("data[0].inst.id", "instId")
    instId = mp.get_extracted_field("instId")
    print(f"提取的instId: {instId}")
    mp.set_header("instId", f"{instId}")

    userName = IG + userName
    print(f"登录接口传的userName: {userName}")
    ##  [用户名授权登录--ShowDoc](https://kf.51tyty.com/doc/web/#/222/18612) 
    # /center/services/rest/user/WeChatAuthorizationLogin/{userName}/{sign}
    print("微信登录接口")
    response = mp.send_request("PUT", f"http://stage2.51tyty.com/center/services/rest/user/WeChatAuthorizationLogin/{userName}/{sign}",save_to_file=True, filename="3微信登录接口.json")
    print(f"状态码: {response.status_code}")
    print("3✅ PUT 微信登录接口 请求测试成功")

    # print("本地微信登录接口")
    # response = mp.send_request("PUT", f"http://127.0.0.1:8115/center/services/rest/user/WeChatAuthorizationLogin/{userName}/{sign}",save_to_file=True, filename="4本地微信登录接口.json")
    # print(f"状态码: {response.status_code}")
    # print("4✅ PUT 本地微信登录接口 请求测试成功")

    mp.extract_field("token", "token")
    token = mp.get_extracted_field("token")
    mp.set_header("token", f"{token}")

    #[获取当前登录用户相关的用户信息和机构信息--ShowDoc](https://kf.51tyty.com/doc/web/#/222/1717) 
    print("微信登录接口")
    response = mp.send_request("GET", f"http://stage2.51tyty.com/user/services/rest/user/MyProfile?industryType=Education",save_to_file=True, filename="5获取当前登录用户相关的用户信息和机构信息.json")
    print(f"状态码: {response.status_code}")
    print("5✅ GET 获取当前登录用户相关的用户信息和机构信息 请求测试成功")

    #[获取当前登录用户相关的用户信息和机构信息--ShowDoc](https://kf.51tyty.com/doc/web/#/222/1717) 
    # print("微信登录接口")
    # response = mp.send_request("GET", f"http://127.0.0.1:8102/user/services/rest/user/MyProfile?industryType=Education",save_to_file=True, filename="6本地获取当前登录用户相关的用户信息和机构信息.json")
    # print(f"状态码: {response.status_code}")
    # print("✅ GET 获取当前登录用户相关的用户信息和机构信息 请求测试成功")

except Exception as e:
    print(f"❌ 请求测试失败: {e}")

