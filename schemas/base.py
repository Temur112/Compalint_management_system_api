from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class BaseComplaint(BaseModel):
    title: str
    desciption: str
    photo_url: str
    amount: float
