from schemas.base import BaseComplaint


class ComplaintIn(BaseComplaint):
    class Config:
        json_schema_extra = {
            "example":{
            "title": "Your title",
            "desciption": "description of complaint",
            "photo_url": "asd.com",
            "amount": 12
            }
        }
