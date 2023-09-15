from typing import Optional, List
from pydantic import BaseModel
from pydantic import Field

# from app.db.schemas.table import TableBase
from app.db.schemas.menu import MenuBase

class ReservateBase(BaseModel):
    table_id: Optional[int]
    menu_id: Optional[int]


class ReservateOut(ReservateBase):
    pass


class ReservateEdit(ReservateBase):
    is_active: Optional[bool]
    

class Reservate(ReservateBase):
    id: Optional[int] 
    
    class Config:
        orm_mode = True