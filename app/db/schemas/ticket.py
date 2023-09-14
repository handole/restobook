from typing import Optional
from pydantic import BaseModel
from pydantic import Field
from datetime import datetime

class TicketBase(BaseModel):
    price: Optional[int] = 2000
    checkin: Optional[datetime]
    checkout: Optional[datetime]
    is_active: Optional[bool]

class TicketOut(TicketBase):
    pass

class TicketEdit(TicketBase):
    is_active: Optional[bool]
    

class Ticket(TicketBase):
    id: Optional[int] 
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    table_id: Optional[int] = Field(default=None, foreign_key="tables.id")
    menu_id: Optional[int] = Field(default=None, foreign_key="menu.id")

    class Config:
        orm_mode = True