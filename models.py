from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///hotel.db', echo=True)

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    bookings = relationship('Booking', back_populates='hotel')

    def __repr__(self):
        return f"Hotel(id={self.id}, name='{self.name}', address='{self.address}')"

    @classmethod
    def create(cls, session, name, address):
        hotel = cls(name=name, address=address)
        session.add(hotel)
        session.commit()
        return hotel

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def update(cls, session, hotel, name=None, address=None):
        if name:
            hotel.name = name
        if address:
            hotel.address = address
        session.commit()
        return hotel

    @classmethod
    def delete(cls, session, hotel):
        session.delete(hotel)
        session.commit()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    check_in = Column(Date)
    check_out = Column(Date)
    hotel = relationship('Hotel', back_populates='bookings')

    def __repr__(self):
        return f"Booking(id={self.id}, hotel_id={self.hotel_id}, check_in='{self.check_in}', check_out='{self.check_out}')"

    @classmethod
    def create(cls, session, hotel_id, check_in, check_out):
        booking = cls(hotel_id=hotel_id, check_in=check_in, check_out=check_out)
        session.add(booking)
        session.commit()
        return booking

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def check_availability(cls, session, hotel_id, check_in, check_out):
        existing_bookings = session.query(cls).filter(
            cls.hotel_id == hotel_id,
            (cls.check_in >= check_in) & (cls.check_in < check_out) |
            (cls.check_out > check_in) & (cls.check_out <= check_out)
        ).all()
        return not existing_bookings

    @classmethod
    def delete(cls, session, booking):
        session.delete(booking)
        session.commit()

def create_tables():
    Base.metadata.create_all(engine)