""" This file contains the models for the items """
from pydantic import BaseModel


class Item(BaseModel):
    """This class contains the model for an item"""

    item_id: int
    name: str
    price: float
    quantity: int


class ItemUpdate(BaseModel):
    """This class contains the model for an item that is being updated"""

    quantity: int
