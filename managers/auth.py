from datetime import datetime, timedelta
import jwt
from decouple import config
from starlette.requests import Request
from typing import Optional
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from db import databse
from models.users import user
from fastapi import HTTPException
from models import RoleType

SECRET_KEY = config("SECRET_KEY")


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            payload = {
                "sub": user["id"],
                "exp": datetime.now() + timedelta(minutes=120),
            }

            return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        except Exception as ex:
            # log th exception
            raise ex


class CustomHTTPBearer(HTTPBearer):
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        try:
            payload = jwt.decode(res.credentials, SECRET_KEY, algorithms="HS256")
            query = user.select().where(user.c.id == payload["sub"])
            userdata = await databse.fetch_one(query)
            request.state.user = userdata
            return userdata
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "Token is invalid")


oauth2_bearer = CustomHTTPBearer()


def is_complainer(request: Request):
    if not request.state.user["role"] == RoleType.complainer:
        raise HTTPException(403, "FORBIDDEN")


def is_approver(request: Request):
    if not request.state.user["role"] == RoleType.approver:
        raise HTTPException(403, "FORBIDDEN")


def is_admin(request: Request):
    if not request.state.user["role"] == RoleType.admin:
        raise HTTPException(403, "FORBIDDEN")
