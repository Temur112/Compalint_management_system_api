from fastapi import APIRouter, Depends
from managers.auth import is_admin, oauth2_bearer
from managers.user import UserManager
from typing import Optional, List
from schemas.response.user import UserOut
from models.enums import RoleType

router = APIRouter(tags=["User"], prefix="/user")


@router.get(
    "/getUsers",
    dependencies=[Depends(oauth2_bearer), Depends(is_admin)],
    response_model=List[UserOut],
)
async def get_all_users():
    return await UserManager.get_all_users()


@router.get(
    "/userByEmail",
    dependencies=[Depends(oauth2_bearer), Depends(is_admin)],
    response_model=List[UserOut],
)
async def get_user_by_email(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_all_users()


@router.put(
    "/{user_id}/make-admin",
    dependencies=[Depends(oauth2_bearer), Depends(is_admin)],
    status_code=204,
)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)


@router.put(
    "/{user_id}/make-approver",
    dependencies=[Depends(oauth2_bearer), Depends(is_admin)],
    status_code=204,
)
async def make_apprver(user_id: int):
    await UserManager.change_role(RoleType.approver, user_id)
