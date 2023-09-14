from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.db import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(15))
    hashed_password = Column(String(250), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
    reservate = relationship("Reservation", back_populates="user")
    ticket = relationship("Ticket", back_populates="user")

    def __repr__(self):
        return 'UserModel(email=%s)' % (self.email) 


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    address = Column(String(250))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    tables = relationship("Tables", back_populates="resto")
    menus = relationship("Menu", back_populates="resto")

    def __repr__(self):
        return 'RestaurantModel(name=%s)' % (self.name)


class Tables(Base):
    __tablename__='tables'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    resto_id = Column(Integer, ForeignKey("restaurants.id"))
    resto = relationship("Restaurant", back_populates="tables")
    reservate = relationship("Reservation", back_populates="table")
    ticket = relationship("Ticket", back_populates="table")

    def __repr__(self):
        return 'TablesModel(number=%s)' % (self.number)


class Menu(Base):
    __tablename__ ='menus'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), index=True, nullable=False)
    price = Column(Integer)
    stock = Column(Integer)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    resto_id = Column(Integer, ForeignKey("restaurants.id"))
    resto = relationship("Restaurant", back_populates="menus")
    reservate = relationship("Reservation", back_populates="menu")
    ticket = relationship("Ticket", back_populates="menu")

    def __repr__(self):
        return 'MenuModel(name=%s)' % (self.name)


class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    is_active = Column(Boolean, default=True)
    user = relationship("User", back_populates="reservate")
    table = relationship("Tables", back_populates="reservate")
    menu = relationship("Menu", back_populates="reservate")

    def __repr__(self):
        return 'ReservationModel(id=%s)' % (self.id)


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    checkin = Column(DateTime)
    checkout = Column(DateTime)
    price = Column(Integer)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    user = relationship("User", back_populates="ticket")
    table = relationship("Tables", back_populates="ticket")
    menu = relationship("Menu", back_populates="ticket")

    def __repr__(self):
        return 'TicketModel(id=%s)' % (self.id)


Base.metadata.create_all(bind=engine)