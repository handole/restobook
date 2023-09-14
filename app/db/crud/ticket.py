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


def get_tickets(db: Session, skip: int = 0,
    limit: int = 100) -> List[ticket_schema.TicketOut]:
    return db.query(Ticket).offset(skip).limit(limit).all()


def create_ticket(db: Session, ticket: ticket_schema.Ticket):
    db_ticket = ticket(
        name=ticket.name,
        stock=ticket.stock,
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