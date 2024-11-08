from sqlalchemy import Column, Integer, String
from app.database import Base

#define database tables for users

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
