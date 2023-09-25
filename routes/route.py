from fastapi import APIRouter
from models.items import Item
from models.orders import Order
from config.database import items_collection, orders_collection
from schema.schemas import individual_item_serial, multiple_item_serial, individual_order_serial, multiple_order_serial
# from bson import ObjectId

router = APIRouter()

@router.get("/")
def say_hello():
    return {"message": "Hello World"}

@router.get("/items")
def get_items():
    items = items_collection.find()
    return multiple_item_serial(items)


@router.get("/orders")
def get_orders():
    orders = orders_collection.find()
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
