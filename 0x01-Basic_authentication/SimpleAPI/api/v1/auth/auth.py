from flask import request

class Auth:
    def require_auth(self, path: str,excluded_paths: List[str]) -> bool:
        return False
    def authorization_header(self, request=None) -> str:
        return None
    def current_user(self, request=None) -> TypeVar('User'): 
        return None