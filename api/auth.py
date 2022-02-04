from os import getenv
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

api_key_header_authorization = APIKeyHeader(name="X-KEY")


def authorize(api_key: str = Depends(api_key_header_authorization)):
    if api_key != getenv("API_KEY"):
        raise HTTPException(status_code=401)
