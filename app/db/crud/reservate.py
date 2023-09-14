from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.models import Reservation
from app.db.schemas import reservate as reservate_schema


def get_reservate(db: Session, reservate_id: int):
    reservate = db.query(Reservation).filter(Reservation.id == reservate_id).first()
    if not reservate:
        raise HTTPException(status_code=404, detail="Reservate Not Found")
    return reservate


def get_reservates(db: Session, user_id: int) -> List[reservate_schema.ReservateOut]:
    return db.query(Reservation).filter(Reservation.user_id == user_id)


def create_reservate(db: Session, reservate: reservate_schema.Reservate):
    db_reservate = reservate(
        name=reservate.name,
        stock=reservate.stock,
        is_active=True,
    )
    db.add(db_reservate)
    db.commit()
    db.refresh(db_reservate)
    return db_reservate


def delete_reservate(db: Session, reservate_id: int):
    reservate = get_reservate(db, reservate_id)
    if not reservate:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="reservate not found")
    db.delete(reservate)
    db.commit()
    return reservate


def edit_reservate(
    db: Session, reservate_id: int, reservate: reservate_schema.ReservateEdit
) -> reservate_schema.Reservate:
    db_reservate = get_reservate(db, reservate_id)
    if not db_reservate:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="reservate not found")
    update_data = reservate.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_reservate, key, value)

    db.add(db_reservate)
    db.commit()
    db.refresh(db_reservate)
    return db_reservate