from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    username = Column(String)
    email = Column(String)
    phone_number = Column(String)
    website = Column(String)