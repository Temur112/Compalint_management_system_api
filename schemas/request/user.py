from schemas.base import UserBase




class UserRegister(UserBase):
    password: str
    phone: str
    first_name: str
    last_name:str
    iban: str

    class Config:
        json_schema_extra = {
            "example":{
            "email": "example@email.com",
            "password": "test123",
            "phone": "991234567",
            "first_name": "Alex",
            "last_name": "Ben",
            "iban": "DE78702202008431447523"
            }
        }

class UserLogin(UserBase):
    password: str
    class Config:
        json_schema_extra = {
            "example":{
            "email": "example@email.com",
            "password": "test123",
            }
        }

