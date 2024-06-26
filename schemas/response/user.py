from schemas.base import UserBase
from models.enums import RoleType


class UserOut(UserBase):
    id: int
    phone: str
    first_name: str
    last_name: str
    role: RoleType
    iban: str
