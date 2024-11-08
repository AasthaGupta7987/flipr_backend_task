from sqlalchemy import Column, Integer, String, Float
from app.database import Base

#tables for products listing

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
