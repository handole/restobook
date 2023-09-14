from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.models import Restaurant
from app.db.schemas import resto as resto_schema


def get_resto(db: Session, resto_id: int):
    resto = db.query(Restaurant).filter(Restaurant.id == resto_id).first()
    if not resto:
        raise HTTPException(status_code=404, detail="This resto not found")
    return resto


def get_restos(db: Session) -> List[resto_schema.RestoOut]:
    return db.query(Restaurant).all()


def create_resto(db: Session, resto: resto_schema.RestoCreate):
    db_resto = Restaurant(
        name=resto.name,
        address=resto.address,
        is_active=True
    )
    db.add(db_resto)
    db.commit()
    db.refresh(db_resto)
    return db_resto


def delete_resto(db: Session, resto_id: int):
    resto = get_resto(db, resto_id)
    if not resto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="This resto not found")
    db.delete(resto)
    db.commit()
    return resto


def edit_resto(
    db: Session, resto_id: int, resto: resto_schema.RestoEdit
) -> resto_schema.Resto:
    db_resto = get_resto(db, resto_id)
    if not db_resto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="This resto not found")
    update_data = resto.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_resto, key, value)

    db.add(db_resto)
    db.commit()
    db.refresh(db_resto)
    return db_resto
