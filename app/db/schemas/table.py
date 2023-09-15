from pydantic import BaseModel
from typing import List

from app.db.schemas.reservate import Reservate

class TableBase(BaseModel):
    number: str
    resto_id: int

class TableOut(TableBase):
    pass

class TableCreate(TableBase):
    pass

class TableEdit(TableBase):
    pass

class Tables(TableBase):
    id: int
    is_active: bool
    reservate: List[Reservate]

    class Config:
        orm_mode = True