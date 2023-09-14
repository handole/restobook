from typing import Optional
from pydantic import BaseModel
from pydantic import Field

class ReservateBase(BaseModel):
    pass

class ReservateOut(ReservateBase):
    pass

class ReservateEdit(ReservateBase):
    is_active: Optional[bool]
    

class Reservate(ReservateBase):
    id: Optional[int] 
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    table_id: Optional[int] = Field(default=None, foreign_key="tables.id")
    menu_id: Optional[int] = Field(default=None, foreign_key="menu.id")

    class Config:
        orm_mode = True