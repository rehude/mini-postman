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

# 测试1: GET请求获取单个资源
print("\n测试: PUT 请求用户名授权登录 小程序")
try:
     # 创建新会话用于PUT请求
    mp.create_session("_session")
    mp.switch_session("_session")
    
    # 设置请求头
    mp.set_headers_from_string(header_string,session="_session")

    # userName = '18870704048'
    userName = '11111188999'
    # 发送PUT请求
    response = mp.send_request("PUT", f"http://stage2.51tyty.com/resource/services/rest/qrcode/WechatLogin/CreateKey/{userName}",title="1微信Sign生成")


    sign = qrCodeKey = mp.extract_field("qrCode.qrCodeKey", "qrCodeKey")

    # 使用提取的userId发送GET请求
    mp.set_param("userId", qrCodeKey)
    mp.set_header("userId", qrCodeKey)
    mp.set_headers_from_string(header_string)

    response = mp.send_request("GET", f"http://stage2.51tyty.com/center/services/rest/user/authorizationRegister/V2/{userName}/{qrCodeKey}",title="2机构列表")
    # response = mp.send_request("GET", f"http://127.0.0.1:8115/center/services/rest/user/authorizationRegister/V2/{userName}/{qrCodeKey}",title="2机构列表")

    i = 0
    #获取必要的请求头参数
    IG = mp.extract_field(f"data[{i}].inst.code", "IG")
    mp.set_header("IG", f"{IG}")
    
    instId = mp.extract_field(f"data[{i}].inst.id", "instId")
    mp.set_header("instId", f"{instId}")

    print(mp.extract_field(f"data[{i}].inst.title","title"))
    # userName = IG + userName
    print(f"登录接口传的userName: {userName}")
    ##  [用户名授权登录--ShowDoc](https://kf.51tyty.com/doc/web/#/222/18612) 
    response = mp.send_request("PUT", f"http://stage2.51tyty.com/center/services/rest/user/WeChatAuthorizationLogin/{userName}/{sign}",title="3微信登录接口")


    token = mp.extract_field("token", "token")
    mp.set_header("token", f"{token}")

    response = mp.send_request("GET", f"http://stage2.51tyty.com/user/services/rest/user/MyProfile?industryType=Education",title="5获取当前登录用户相关的用户信息和机构信息")
    # #[获取当前登录用户相关的用户信息和机构信息--ShowDoc](https://kf.51tyty.com/doc/web/#/222/1717) 

except Exception as e:
    print(f"❌ 请求测试失败: {e}")

