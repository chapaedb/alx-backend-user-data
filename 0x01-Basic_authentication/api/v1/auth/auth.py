#!/usr/bin/env python3
"""Authentication module.
"""
from flask import request
from typing import List, TypeVar
import fnmatch

class Auth:

    def require_auth(self, path: str,excluded_paths: List[str]) -> bool:
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded in excluded_paths:
            if path == excluded.rstrip('/'):
                return False
        return True
    def authorization_header(self, request=None) -> str:
        return None
    def current_user(self, request=None) -> TypeVar('User'): 
        return None