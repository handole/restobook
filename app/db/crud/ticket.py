from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.models import Ticket
from app.db.schemas import ticket as ticket_schema



def get_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="ticket Not Found")
    return ticket


def get_tickets(db: Session, user_id: int) -> List[ticket_schema.TicketOut]:
    return db.query(Ticket).filter(Ticket.user_id == user_id).all()


def create_ticket(db: Session, data: ticket_schema.TicketCreate, user_id):
    db_ticket = Ticket(
        price=data.price,
        checkin=data.checkin,
        checkout=data.checkout,
        table_id=data.table_id,
        menu_id=data.menu_id,
        user_id=user_id,
        is_active=True,
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def delete_ticket(db: Session, ticket_id: int):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="ticket not found")
    db.delete(ticket)
    db.commit()
    return ticket


def edit_ticket(
    db: Session, ticket_id: int, ticket: ticket_schema.TicketEdit
) -> ticket_schema.Ticket:
    db_ticket = get_ticket(db, ticket_id)
    if not db_ticket:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="ticket not found")
    update_data = ticket.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_ticket, key, value)

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket