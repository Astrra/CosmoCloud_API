from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    productId: int
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class Order(BaseModel):
    order_id: int
    timestamp: str
    items: List[Item]
    total_amount: float
    user_address: UserAddress

class PlaceOrder(BaseModel):
    items: List[Item]
    user_address: UserAddress