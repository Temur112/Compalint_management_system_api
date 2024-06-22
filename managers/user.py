from passlib.context import CryptContext
from fastapi import HTTPException
from db import databse
from models.users import user
from asyncpg import UniqueViolationError
from managers.auth import AuthManager
from models.enums import RoleType

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



class UserManager:

    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])

        try:
            id_ = await databse.execute(user.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email already registered")
        
        user_do = await databse.fetch_one(user.select().where(user.c.id == id_))

        return AuthManager.encode_token(user_do)
    
    @staticmethod
    async def login(user_data):
        user_do = await databse.fetch_one(user.select().where(user.c.email == user_data["email"]))
        if not user_do:
            raise HTTPException(400, "Wrong email or password")
        elif not pwd_context.verify(user_data["password"], user_do["password"]):
            raise HTTPException(400, "Wrong email or password")
        
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_all_users():
        return await databse.fetch_all(user.select())

    @staticmethod
    async def get_user_by_email(email):
        return await databse.fetch_all(user.select().where(user.c.email == email))
    

    @staticmethod
    async def change_role(role: RoleType, user_id):
        await databse.execute(user.update().where(user.c.id == user_id).values(role=role))


