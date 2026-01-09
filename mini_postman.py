import requests
import json
from typing import Dict, Any, Optional, Union
from copy import deepcopy

class MiniPostman:
    """轻量级HTTP请求工具"""
    
    def __init__(self):
        self.sessions: Dict[str, Any] = {}
        self.current_session = "default"
        self.sessions[self.current_session] = {
            "headers": {},
            "params": {},
            "data": {},
            "json": {},
            "response": None,
            "extracted_fields": {}
        }
    
    def set_header(self, key: str, value: str, session: Optional[str] = None) -> None:
        """设置请求头"""
        session = session or self.current_session
        self.sessions[session]["headers"][key] = value
    
    def set_headers_from_string(self, headers_string: str, session: Optional[str] = None) -> None:
        """从字符串批量设置请求头，格式为每行一个header: Key: Value"""
        session = session or self.current_session
        headers = self.sessions[session]["headers"]
        
        # 按行分割字符串
        lines = headers_string.strip().split('\n')
        
        for line in lines:
            # 跳过空行
            if not line.strip():
                continue
            
            # 分割键值对
            parts = line.split(':', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                headers[key] = value
    
    def set_param(self, key: str, value: Any, session: Optional[str] = None) -> None:
        """设置查询参数"""
        session = session or self.current_session
        self.sessions[session]["params"][key] = value
    
    def set_data(self, key: str, value: Any, session: Optional[str] = None) -> None:
        """设置表单数据"""
        session = session or self.current_session
        self.sessions[session]["data"][key] = value
    
    def set_json(self, data: Dict[str, Any], session: Optional[str] = None) -> None:
        """设置JSON数据"""
        session = session or self.current_session
        self.sessions[session]["json"] = data
    
    def send_request(self, method: str, url: str, session: Optional[str] = None, title: str = "", save_to_file: bool = True, filename: str = "response.json", verify: bool = False, proxies: Optional[Dict[str, str]] = None, **kwargs) -> Any:
        """发送HTTP请求"""
        session = session or self.current_session
        session_data = self.sessions[session]
        
        # URL 验证和修复：确保URL包含协议前缀
        if not url.startswith(('http://', 'https://')):
            # 默认添加http://协议前缀
            url = f"http://{url}"
            print(f"⚠️  URL 缺少协议前缀，已自动添加 http://，修复后的URL: {url}")
        
        # 打印接口信息
        print(f"\n=== {title if title else '接口请求'} ===")
        print(f"请求方式: {method}")
        print(f"请求URL: {url}")
        print(f"SSL验证: {verify}")
        print(f"代理设置: {'禁用' if proxies is None else proxies}")
        
        # 如果没有指定filename，使用title作为文件名
        if filename == "response.json" and title:
            # 处理title作为文件名，替换特殊字符，确保合法性
            import re
            # 替换非字母数字字符为下划线
            safe_title = re.sub(r'[^\w\-\.]', '_', title)
            # 确保文件名以.json结尾
            if not safe_title.endswith('.json'):
                safe_title = f"{safe_title}.json"
            filename = safe_title
        
        # 构建请求参数
        request_kwargs = {
            "headers": session_data["headers"],
            "params": session_data["params"],
            "verify": verify,  # 添加verify参数
        }
        
        # 添加代理设置，如果为None则使用系统代理，{}则禁用代理
        if proxies is not None:
            request_kwargs["proxies"] = proxies
        elif "no_proxy" in kwargs and kwargs["no_proxy"]:
            # 禁用代理
            request_kwargs["proxies"] = {}
        
        if session_data["data"]:
            request_kwargs["data"] = session_data["data"]
        if session_data["json"]:
            request_kwargs["json"] = session_data["json"]
        
        # 保存请求信息到文件
        self.save_request_to_file(method, url, request_kwargs, title, session=session)
        
        # 发送真正的HTTP请求
        response = requests.request(method, url, **request_kwargs)
        
        # 保存响应
        session_data["response"] = response
        
        # 打印响应信息
        print(f"响应状态码: {response.status_code}")
        
        # 自动保存响应到文件
        if save_to_file:
            self.save_response_to_file(session=session, filename=filename, title=title)
        
        return response
    
    def save_request_to_file(self, method: str, url: str, request_kwargs: Dict[str, Any], title: str, session: Optional[str] = None, filename: str = "request.json") -> None:
        """将请求信息保存到当天日期/request/目录下的文件中"""
        import os
        from datetime import datetime
        
        session = session or self.current_session
        
        try:
            # 获取当天日期，格式为 YYYY.MM.DD
            today = datetime.now().strftime("%Y.%m.%d")
            
            # 构建请求目录路径：当天日期/request
            # 处理title作为文件名，替换特殊字符，确保合法性
            import re
            safe_title = re.sub(r'[^\w\-\.]', '_', title)
            # 确保文件名以.json结尾
            if not safe_title.endswith('.json'):
                safe_title = f"{safe_title}.json"
            
            # 构建目录：根目录/2026.01.08/request
            request_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), today, "request")
            os.makedirs(request_dir, exist_ok=True)
            
            # 构建文件路径：根目录/2026.01.08/request/标题.json
            file_path = os.path.join(request_dir, safe_title)
            
            # 构建请求信息
            request_info = {
                "method": method,
                "url": url,
                "timestamp": datetime.now().isoformat(),
                "headers": request_kwargs.get("headers", {}),
                "params": request_kwargs.get("params", {}),
                "data": request_kwargs.get("data", {}),
                "json": request_kwargs.get("json", {})
            }
            
            # 写入JSON文件，缩进2，确保中文正常显示
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(request_info, f, ensure_ascii=False, indent=2)
            
            print(f"✅ 请求信息已保存到: {file_path}")
        except Exception as e:
            raise Exception(f"保存请求信息到文件失败: {e}")
    
    def save_response_to_file(self, method: str = "", url: str = "", request_kwargs: Dict[str, Any] = {}, title: str = "", session: Optional[str] = None, filename: str = "response.json") -> None:
        """将响应JSON保存到当天日期/response文件夹下的文件中，覆盖原有内容"""
        import os
        from datetime import datetime
        
        session = session or self.current_session
        session_data = self.sessions[session]
        
        if not session_data["response"]:
            raise ValueError("没有可用的响应数据")
        
        try:
            # 获取响应JSON
            response_json = session_data["response"].json()
            
            # 获取当天日期，格式为 YYYY.MM.DD
            today = datetime.now().strftime("%Y.%m.%d")
            
            # 处理title作为文件名，替换特殊字符，确保合法性
            import re
            safe_title = re.sub(r'[^\w\-\.]', '_', title)
            # 确保文件名以.json结尾
            if not safe_title.endswith('.json'):
                safe_title = f"{safe_title}.json"
            
            # 构建响应目录路径：当天日期/response
            response_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), today, "response")
            os.makedirs(response_dir, exist_ok=True)
            
            # 构建文件路径：根目录/2026.01.08/response/标题.json
            file_path = os.path.join(response_dir, safe_title)
            
            # 写入JSON文件，缩进2，确保中文正常显示
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(response_json, f, ensure_ascii=False, indent=2)
            
            print(f"✅ 响应JSON已保存到: {file_path}")
        except ValueError:
            raise ValueError("响应不是有效的JSON格式")
        except Exception as e:
            raise Exception(f"保存响应到文件失败: {e}")
    
    def get_response(self, session: Optional[str] = None) -> Any:
        """获取响应对象"""
        session = session or self.current_session
        return self.sessions[session]["response"]
    
    def get_response_text(self, session: Optional[str] = None) -> str:
        """获取响应文本"""
        session = session or self.current_session
        response = self.sessions[session]["response"]
        return response.text if response else ""
    
    def get_response_json(self, session: Optional[str] = None) -> Dict[str, Any]:
        """获取响应JSON"""
        session = session or self.current_session
        response = self.sessions[session]["response"]
        return response.json() if response else {}
    
    def extract_field(self, field_path: str, alias: str, session: Optional[str] = None) -> Any:
        """从响应中提取字段，支持嵌套路径和数组索引，如 "data[0].inst.code"""
        session = session or self.current_session
        response_json = self.get_response_json(session)
        
        value = response_json
        current_path = ""
        
        try:
            # 解析字段路径，支持数组索引
            import re
            # 将路径拆分为键列表，支持数组索引格式如 data[0].inst.code
            path_parts = re.split(r'\.|(?=\[\d+\])', field_path)
            
            for part in path_parts:
                part = part.strip()
                if not part:
                    continue
                
                current_path = f"{current_path}.{part}" if current_path else part
                
                # 处理数组索引，如 [0]
                if part.startswith('[') and part.endswith(']'):
                    # 提取索引值
                    index = int(part[1:-1])
                    # 检查是否为空数组
                    if isinstance(value, list):
                        if len(value) == 0:
                            raise IndexError(f"数组 '{current_path[:-len(part)]}' 为空，无法访问索引 {index}")
                        if index >= len(value):
                            raise IndexError(f"数组 '{current_path[:-len(part)]}' 长度为 {len(value)}，无法访问索引 {index}")
                    value = value[index]
                else:
                    # 处理普通键
                    value = value[part]
            
            # 保存提取的字段
            self.sessions[session]["extracted_fields"][alias] = value
            
            # 打印提取的字段
            print(f"✅ 提取字段: {field_path} = {value} (别名为 '{alias}')")
            
            # 直接返回提取的值
            return value
        except (KeyError, TypeError, IndexError) as e:
            # 提供更详细的错误信息
            if isinstance(e, IndexError):
                raise ValueError(f"字段路径 '{field_path}' 访问失败：{str(e)}")
            else:
                raise ValueError(f"字段路径 '{field_path}' 在响应中不存在，当前路径 '{current_path}' 访问失败：{str(e)}")
    
    def get_extracted_field(self, alias: str, session: Optional[str] = None) -> Any:
        """获取提取的字段值"""
        session = session or self.current_session
        return self.sessions[session]["extracted_fields"].get(alias)
    
    def create_session(self, name: str, copy_from: Optional[str] = None) -> None:
        """创建新会话，可以从现有会话复制"""
        if copy_from and copy_from in self.sessions:
            # 深拷贝现有会话
            self.sessions[name] = deepcopy(self.sessions[copy_from])
            # 重置响应和提取的字段
            self.sessions[name]["response"] = None
            self.sessions[name]["extracted_fields"] = {}
        else:
            # 创建新的空会话
            self.sessions[name] = {
                "headers": {},
                "params": {},
                "data": {},
                "json": {},
                "response": None,
                "extracted_fields": {}
            }
    
    def switch_session(self, name: str) -> None:
        """切换会话"""
        if name not in self.sessions:
            raise ValueError(f"会话 '{name}' 不存在")
        self.current_session = name
    
    def delete_session(self, name: str) -> None:
        """删除会话"""
        if name in self.sessions and name != "default":
            del self.sessions[name]
            if self.current_session == name:
                self.current_session = "default"
    
    def list_sessions(self) -> list:
        """列出所有会话"""
        return list(self.sessions.keys())
    
    def clear_session(self, session: Optional[str] = None) -> None:
        """清空会话数据"""
        session = session or self.current_session
        self.sessions[session] = {
            "headers": {},
            "params": {},
            "data": {},
            "json": {},
            "response": None,
            "extracted_fields": {}
        }
    
    def update_from_extracted(self, target: str, key: str, alias: str, session: Optional[str] = None) -> None:
        """使用提取的字段更新请求参数"""
        session = session or self.current_session
        value = self.get_extracted_field(alias, session)
        if value is None:
            raise ValueError(f"提取的字段 '{alias}' 不存在")
        
        if target == "header":
            self.set_header(key, str(value), session)
        elif target == "param":
            self.set_param(key, value, session)
        elif target == "data":
            self.set_data(key, value, session)
        elif target == "json":
            self.sessions[session]["json"][key] = value
        else:
            raise ValueError(f"无效的目标 '{target}'")
