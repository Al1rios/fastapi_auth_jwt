from datetime import datetime, timedelta
from os import getenv

from fastapi.responses import JSONResponse
from jwt import decode, encode, exceptions


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)  # numbers days
    return new_date


def write_token(data: dict):
    token = encode(
        payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256"
    )
    return token


def validate_token(token, output=False):
    try:
        if output:
            decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)