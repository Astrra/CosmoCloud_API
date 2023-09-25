""" This file contains the models for the orders service. """
from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    """This class contains the model for an item in the order."""

    productId: int
    boughtQuantity: int


class UserAddress(BaseModel):
    """This class contains the model for the user's address."""

    city: str
    country: str
    zip_code: str


class Order(BaseModel):
    """This class contains the model for an order."""

    order_id: int
    timestamp: str
    items: List[Item]
    total_amount: float
    user_address: UserAddress


class PlaceOrder(BaseModel):
    """This class contains the model for an order that is being placed."""

    items: List[Item]
    user_address: UserAddress
