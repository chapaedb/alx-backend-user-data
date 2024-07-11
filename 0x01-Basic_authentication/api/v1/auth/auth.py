#!/usr/bin/env python3
"""Authentication module.
"""
from flask import request
from typing import List, TypeVar
import fnmatch

class Auth:
    """
    Authorization required functionalities require this
    """
    def require_auth(self, path: str,excluded_paths: List[str]) -> bool:
        """Returns True if the path is not in the list of strings excluded_paths"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path = path + '/'

        for excluded in excluded_paths:
            if excluded[-1] != '/':
                excluded = excluded + '/'

            if path == excluded:
                return False
        return True
    def authorization_header(self, request=None) -> str:
        return None
    def current_user(self, request=None) -> TypeVar('User'): 
        return None