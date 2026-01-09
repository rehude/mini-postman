import sys
import os

# 添加父目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mini_postman import MiniPostman

# 创建MiniPostman实例
mp = MiniPostman()
# http://stage2.51tyty.com/resource/services/rest/qrcode/WechatLogin/CreateKey/sjjjk11112138714
from httpRequest import HttpRequest
hr = HttpRequest()
# 设置请求头
header_string = """
Content-Type:application/json
DeviceType:4
language:ch
lan:ch
AppVersion:2.15.29.20251230
DeviceUniqueId:weixinmp_oyDkc5NoGpVsJF5KumevFjNXk4JI
openId:oyDkc5NoGpVsJF5KumevFjNXk4JI
industryType:Education
AppType:0
FromAppName:wechatClient
instId:17
serverId:1201
"""

# 测试1: GET请求获取单个资源

try:
     # 创建新会话用于PUT请求
    
    # 设置请求头
    hr.set_headers_from_string(header_string)
    userName = 'bwxmn913'
    # userName = '11112138714'
    # 发送PUT请求
    # response = mp.send_request("PUT", f"http://stage2.51tyty.com/resource/services/rest/qrcode/WechatLogin/CreateKey/{userName}",title="1微信Sign生成")
    # hr.PUT(f"http://stage2.51tyty.com/resource/services/rest/qrcode/WechatLogin/CreateKey/{userName}",title="微信Sign生成", no_proxy=True)

    # hr.GET(f"https://stage2.51tyty.com/social/services/rest/group/Groups/Mine/V2?startPos=0&endPos=19&search=",title="微信Sign生成")
    # hr.GET(f"http://localhost:8103/social/services/rest/group/Groups/Mine/V2?startPos=0&endPos=19&search=",title="微信Sign生成", no_proxy=True)
    hr.GET("https://stage2.51tyty.com/user/services/rest/userInner/CheckUser/1007178:1830932143:fd48127d-c1a3-4b38-8047-046112beb253:4005181c9828f296da84c3307c3aaa05:1201v",title="检查token",no_proxy=True)
    # hr.GET("http://127.0.0.1:8102/user/services/rest/userInner/CheckUser/1007178:1830932143:fd48127d-c1a3-4b38-8047-046112beb253:4005181c9828f296da84c3307c3aaa05:1201v",title="检查token",no_proxy=True)


except Exception as e:
    print(f"❌ 请求测试失败: {e}")

