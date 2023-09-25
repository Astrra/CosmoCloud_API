from fastapi import APIRouter
from models.items import Item
from models.orders import Order
from config.database import items_collection, orders_collection
from schema.schemas import individual_item_serial, multiple_item_serial, individual_order_serial, multiple_order_serial
from fastapi import HTTPException


router = APIRouter()

@router.get("/")
def say_hello():
    return {"message": "Hello World"}

@router.get("/items")
def get_items(limit: int = 10, offset: int = 0):
    items = items_collection.find().skip(offset).limit(limit)
    if items is None:
        raise HTTPException(status_code=404, detail="No items found.")
    return multiple_item_serial(items)

@router.get("/items/{item_id}")
def get_item(item_id: int):
    item = items_collection.find_one({"item_id": item_id})
    return individual_item_serial(item)

@router.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    orders = orders_collection.find().skip(offset).limit(limit)
    if orders is None:
        raise HTTPException(status_code=404, detail="No orders found.")
    return multiple_order_serial(orders)

@router.get("/orders/{order_id}")
def get_order(order_id: int):
    order = orders_collection.find_one({"order_id": order_id})
    return individual_order_serial(order)

@router.post("/place-order")
def place_order(order: Order):
    order_dict= order.dict(by_alias=True)
    orders_collection.insert_one(order_dict)
    return individual_order_serial(order_dict)