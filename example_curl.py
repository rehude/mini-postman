from httpRequest import HttpRequest

# 创建 HttpRequest 实例
hr = HttpRequest()

# 示例 curl 命令
curl_command = '''curl -X POST "http://127.0.0.1:8000/ask" \ 
   -H "Content-Type: application/json" \ 
   -d '{ 
     "question": "LangChain 是什么？", 
     "model_name": "qwen3-max-preview", 
     "temperature": 0, 
     "max_tokens": 512 
   }' '''

# 使用 from_curl 方法发送请求
print("使用 curl 命令发送请求:")
print(curl_command)
print("\n正在处理...")

try:
    # 发送请求
    response = hr.from_curl(curl_command, title="LangChain 相关问题")
    
    # 获取响应
    print("\n响应状态码:", response.status_code)
    print("响应内容:", response.text)
except Exception as e:
    print(f"\n错误: {e}")
    print("注意: 这可能是因为目标服务器未运行，请确保服务器在指定端口上运行")