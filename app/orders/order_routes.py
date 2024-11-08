from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.orders.models import Order
from app.cart.models import CartItem
from app.schemas import OrderCreate

router = APIRouter()

#routes for order

@router.post("/place")
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == order.user_id).all()
    if not cart_items:
        raise HTTPException(status_code=404, detail="Cart is empty")

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    new_order = Order(user_id=order.user_id, total_price=total_price)
    db.add(new_order)
    db.query(CartItem).filter(CartItem.user_id == order.user_id).delete()
    db.commit()
    db.refresh(new_order)
    return new_order
