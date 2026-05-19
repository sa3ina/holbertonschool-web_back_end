from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if authentication is required, otherwise False
        """

        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        # normalize path (slash tolerant)
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
