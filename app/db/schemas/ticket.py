from typing import Optional, List
from pydantic import BaseModel
from pydantic import Field
from datetime import datetime

from app.db.schemas.table import TableBase
from app.db.schemas.menu import MenuBase


class TicketBase(BaseModel):
    price: Optional[int] = 2000
    checkin: Optional[datetime]
    checkout: Optional[datetime]  

class TicketOut(TicketBase):
    pass

class TicketCreate(TicketBase):
    table_id: Optional[int]
    menu_id: Optional[int]


class TicketEdit(TicketBase):
    is_active: Optional[bool]
    

class Ticket(TicketBase):
    id: Optional[int] 
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    
    class Config:
        orm_mode = True