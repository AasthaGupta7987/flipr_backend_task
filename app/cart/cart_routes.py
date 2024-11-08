from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.cart.models import CartItem
from app.products.models import Product
from app.schemas import CartItemCreate, CartItemUpdate

router = APIRouter()

#routes for cart section

@router.post("/add")
def add_to_cart(cart_item: CartItemCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_cart_item = db.query(CartItem).filter(
        CartItem.user_id == cart_item.user_id,
        CartItem.product_id == cart_item.product_id
    ).first()
    if existing_cart_item:
        existing_cart_item.quantity += cart_item.quantity
        db.commit()
        db.refresh(existing_cart_item)
        return existing_cart_item
    new_cart_item = CartItem(**cart_item.dict())
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)
    return new_cart_item

@router.put("/update")
def update_cart(cart_item: CartItemUpdate, db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(
        CartItem.user_id == cart_item.user_id,
        CartItem.product_id == cart_item.product_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not in cart")
    item.quantity = cart_item.quantity
    db.commit()
    db.refresh(item)
    return item

@router.delete("/delete/{product_id}")
def delete_from_cart(user_id: int, product_id: int, db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == product_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    db.delete(item)
    db.commit()
    return {"detail": "Item removed from cart"}
