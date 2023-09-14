from pydantic import BaseModel
from typing import Optional, List

from app.db.schemas.reservate import Reservate


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    phone_number: Optional[str]
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

    
class UserOut(UserBase):
    pass

class UserCreate(UserBase):
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "test",
                "last_name": "user",
                "email": "usertest@mail.com",
                "phone_number": "0123123213",
                "is_active": True,
                "is_superuser": False,
                "password": "tes123"
            }
        }
        orm_mode = True

class UserEdit(UserBase):
    password: Optional[str]

    class Config:
        orm_mode = True

class User(UserBase):
    id: Optional[int]
    reservate: List[Reservate]

    class Config:
        orm_mode = True
        
class Token(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]

class TokenData(BaseModel):
    email: Optional[str]
    permissions: Optional[str] = "user"
