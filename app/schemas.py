from pydantic import BaseModel
from typing import Optional

#schemas for the all functions

# User schemas
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    address: Optional[str] = None

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    address: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

# Product schemas
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None

# Cart schemas
class CartItemCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartItemUpdate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

# Order schema
class OrderCreate(BaseModel):
    user_id: int
