from mini_postman import MiniPostman
from typing import Dict, Any, Optional

class HttpRequest:
    """HTTP请求封装类，简化GET、POST、PUT方法调用"""
    
    def __init__(self):
        # 创建MiniPostman实例
        self.mp = MiniPostman()
    
    def GET(self, url: str, title: str = "GET请求", **kwargs) -> Any:
        """发送GET请求
        
        Args:
            url: 请求URL
            title: 接口标题，用于生成文件名
            **kwargs: 其他参数（session, headers, params, proxies, no_proxy等）
            
        Returns:
            响应对象
        """
        # 处理可选参数
        session = kwargs.get("session")
        
        # 设置请求头
        if "headers" in kwargs:
            for key, value in kwargs["headers"].items():
                self.mp.set_header(key, value, session=session)
        
        # 设置查询参数
        if "params" in kwargs:
            for key, value in kwargs["params"].items():
                self.mp.set_param(key, value, session=session)
        
        # 发送GET请求
        return self.mp.send_request("GET", url, session=session, title=title, **kwargs)
    
    def POST(self, url: str, title: str = "POST请求", **kwargs) -> Any:
        """发送POST请求
        
        Args:
            url: 请求URL
            title: 接口标题，用于生成文件名
            **kwargs: 其他参数（session, headers, data, json等）
            
        Returns:
            响应对象
        """
        # 处理可选参数
        session = kwargs.get("session")
        
        # 设置请求头
        if "headers" in kwargs:
            for key, value in kwargs["headers"].items():
                self.mp.set_header(key, value, session=session)
        
        # 设置表单数据
        if "data" in kwargs:
            for key, value in kwargs["data"].items():
                self.mp.set_data(key, value, session=session)
        
        # 设置JSON数据
        if "json" in kwargs:
            self.mp.set_json(kwargs["json"], session=session)
        
        # 发送POST请求
        return self.mp.send_request("POST", url, session=session, title=title, **kwargs)
    
    def PUT(self, url: str, title: str = "PUT请求", **kwargs) -> Any:
        """发送PUT请求
        
        Args:
            url: 请求URL
            title: 接口标题，用于生成文件名
            **kwargs: 其他参数（session, headers, data, json等）
            
        Returns:
            响应对象
        """
        # 处理可选参数
        session = kwargs.get("session")
        
        # 设置请求头
        if "headers" in kwargs:
            for key, value in kwargs["headers"].items():
                self.mp.set_header(key, value, session=session)
        
        # 设置表单数据
        if "data" in kwargs:
            for key, value in kwargs["data"].items():
                self.mp.set_data(key, value, session=session)
        
        # 设置JSON数据
        if "json" in kwargs:
            self.mp.set_json(kwargs["json"], session=session)
        
        # 发送PUT请求
        return self.mp.send_request("PUT", url, session=session, title=title, **kwargs)
    
    def extract(self, field_path: str, alias: str, session: Optional[str] = None) -> Any:
        """提取响应字段
        
        Args:
            field_path: 字段路径，如 "data[0].id"
            alias: 字段别名
            session: 会话名称
            
        Returns:
            提取的字段值
        """
        return self.mp.extract_field(field_path, alias, session=session)
    
    def get_response_json(self, session: Optional[str] = None) -> Dict[str, Any]:
        """获取响应JSON
        
        Args:
            session: 会话名称
            
        Returns:
            响应JSON字典
        """
        return self.mp.get_response_json(session=session)
    
    def get_response_text(self, session: Optional[str] = None) -> str:
        """获取响应文本
        
        Args:
            session: 会话名称
            
        Returns:
            响应文本字符串
        """
        return self.mp.get_response_text(session=session)
    
    def set_headers_from_string(self, headers_string: str, session: Optional[str] = None) -> None:
        """从字符串批量设置请求头
        
        Args:
            headers_string: 请求头字符串，格式为每行一个 "Key: Value"
            session: 会话名称
        """
        self.mp.set_headers_from_string(headers_string, session=session)
    
    def set_header(self, key: str, value: str, session: Optional[str] = None) -> None:
        """设置单个请求头
        
        Args:
            key: 请求头键
            value: 请求头值
            session: 会话名称
        """
        self.mp.set_header(key, value, session=session)
    
    def set_param(self, key: str, value: Any, session: Optional[str] = None) -> None:
        """设置查询参数
        
        Args:
            key: 参数键
            value: 参数值
            session: 会话名称
        """
        self.mp.set_param(key, value, session=session)
    
    def set_json(self, data: Dict[str, Any], session: Optional[str] = None) -> None:
        """设置JSON数据

        Args:
            data: JSON数据字典
            session: 会话名称
        """
        self.mp.set_json(data, session=session)
    
    def from_curl(self, curl_command: str, title: str = "CURL请求", session: Optional[str] = None, **kwargs) -> Any:
        """从curl命令发送请求

        Args:
            curl_command: curl命令字符串
            title: 接口标题，用于生成文件名
            session: 会话名称
            **kwargs: 其他参数（verify, proxies等）

        Returns:
            响应对象
        """
        import re
        
        # 清理curl命令，去除转义字符和换行
        curl_command = curl_command.replace('\\', '').replace('\n', '').strip()
        
        # 提取请求方法
        method_match = re.search(r'-X\s+(\w+)', curl_command, re.IGNORECASE)
        method = method_match.group(1).upper() if method_match else 'GET'
        
        # 提取URL
        url_match = re.search(r'"([^"]+)"', curl_command)
        if not url_match:
            raise ValueError("无法从curl命令中提取URL")
        url = url_match.group(1)
        
        # 提取请求头
        headers = {}
        header_matches = re.findall(r'-H\s+"([^"]+)"', curl_command)
        for header in header_matches:
            if ':' in header:
                key, value = header.split(':', 1)
                headers[key.strip()] = value.strip()
        
        # 提取请求体
        data_match = re.search(r'-d\s+\'([^\']+)\'', curl_command)
        json_data = {}
        if data_match:
            data_str = data_match.group(1)
            try:
                json_data = eval(data_str)
            except:
                pass
        
        # 清理会话数据
        self.mp.clear_session(session=session)
        
        # 设置请求头
        for key, value in headers.items():
            self.mp.set_header(key, value, session=session)
        
        # 设置JSON数据
        if json_data:
            self.mp.set_json(json_data, session=session)
        
        # 发送请求
        return self.mp.send_request(method, url, session=session, title=title, **kwargs)
