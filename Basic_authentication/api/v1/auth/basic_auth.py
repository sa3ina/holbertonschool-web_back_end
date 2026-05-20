#!/usr/bin/env python3
''' Module of Basic_auth
'''
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    ''' BasicAuth class
    '''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' def extract base64 authorization header '''

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' def decode base64 authorization header '''

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(
                base64_authorization_header
            )
            return decoded.decode('utf-8')
        except Exception:
            return None
    

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' def extract user credentials '''
        
        if decoded_base64_authorization_header is None:
          return None, None

        if not isinstance(
            decoded_base64_authorization_header, str):
          return None, None

        if ':' not in decoded_base64_authorization_header:
          return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]
