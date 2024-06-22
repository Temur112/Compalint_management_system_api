from fastapi import APIRouter
from managers.user import UserManager
from schemas.request.user import UserRegister, UserLogin


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register/", status_code=201)
async def register(user_data: UserRegister):
    token = await UserManager.register(user_data.model_dump())
    return {"token": token}

@router.post("/login/")
async def login(user_data: UserLogin):
    token = await UserManager.login(user_data.model_dump())
    return {
        "token": token
    }