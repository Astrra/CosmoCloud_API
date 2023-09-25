from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    productId: int
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class Orders(BaseModel):
    timestamp: str
    items: List[Item]
    total_amount: float
    user_address: UserAddress