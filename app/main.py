from fastapi import FastAPI
from auth.auth_routes import router as auth_router
from products.product_routes import router as product_router
from cart.cart_routes import router as cart_router
from orders.order_routes import router as order_router

app = FastAPI()

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(cart_router, prefix="/cart", tags=["cart"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
