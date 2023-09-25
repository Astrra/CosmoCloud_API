"""This module contains the routes for the CosmoCloud API."""

from datetime import datetime
from fastapi import APIRouter, HTTPException
from models.items import Item, ItemUpdate
from models.orders import Order, PlaceOrder
from config.database import items_collection, orders_collection
from schema.schemas import (
    individual_item_serial,
    multiple_item_serial,
    individual_order_serial,
    multiple_order_serial,
)

router = APIRouter()


@router.get("/")
def say_hello():
    """
    Returns a JSON response with a message indicating that the CosmoCloud API is running.

    Returns:
        dict: A dictionary containing a single key-value pair with the message.
    """
    return {"message": "CosmoCloud API is running!"}


@router.get("/items")
async def get_items(limit: int = 10, offset: int = 0):
    """
    Returns a JSON response with a list of items from the database.

    Args:
        limit (int, optional): The maximum number of items to return. Defaults to 10.
        offset (int, optional): The number of items to skip before returning results. Defaults to 0.

    Raises:
        HTTPException: If no items are found in the database.

    Returns:
        dict: A dictionary containing a list of items.
    """
    items = items_collection.find().skip(offset).limit(limit)
    if not items:
        raise HTTPException(status_code=404, detail="No items found.")
    return multiple_item_serial(items)


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    """
    Returns a JSON response with the details of a single item from the database.

    Args:
        item_id (int): The ID of the item to retrieve.

    Raises:
        HTTPException: If no item with the specified ID is found in the database.

    Returns:
        dict: A dictionary containing the details of the item.
    """
    item = items_collection.find_one({"item_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="No item found.")
    return individual_item_serial(item)


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemUpdate):
    """
    Updates the quantity of an item in the database and returns a JSON response with the updated item details.

    Args:
        item_id (int): The ID of the item to update.
        item (ItemUpdate): An object containing the new quantity value.

    Raises:
        HTTPException: If no item with the specified ID is found in the database.

    Returns:
        dict: A dictionary containing the updated details of the item.
    """
    item_to_be_updated = items_collection.find_one({"item_id": item_id})
    if item_to_be_updated is None:
        raise HTTPException(status_code=404, detail="No item found.")
    new_values = {"$set": {"quantity": item.quantity}}
    items_collection.update_one({"item_id": item_id}, new_values)
    item_to_be_updated = items_collection.find_one({"item_id": item_id})
    return individual_item_serial(item_to_be_updated)


@router.get("/orders")
async def get_orders(limit: int = 10, offset: int = 0):
    """
    Returns a JSON response with a list of orders from the database.

    Args:
        limit (int, optional): The maximum number of orders to return. Defaults to 10.
        offset (int, optional): The number of orders to skip before returning results. Defaults to 0.

    Raises:
        HTTPException: If no orders are found in the database.

    Returns:
        dict: A dictionary containing a list of orders.
    """
    orders = orders_collection.find().skip(offset).limit(limit)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found.")
    return multiple_order_serial(orders)


@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    """
    Returns a JSON response with the details of a single order from the database.

    Args:
        order_id (int): The ID of the order to retrieve.

    Raises:
        HTTPException: If no order with the specified ID is found in the database.

    Returns:
        dict: A dictionary containing the details of the order.
    """
    order = orders_collection.find_one({"order_id": order_id})
    if order is None:
        raise HTTPException(status_code=404, detail="No order found.")
    return individual_order_serial(order)


@router.post("/place-order")
async def place_order(order: PlaceOrder):
    """
    Places an order in the database and returns a JSON response with the details of the order.

    Args:
        order (PlaceOrder): An object containing the details of the order.

    Raises:
        HTTPException: If an item in the order is not found in the database or if there are not enough items in stock.

    Returns:
        dict: A dictionary containing the details of the order.
    """
    order_dict = order.dict(by_alias=True)
    order_dict["order_id"] = orders_collection.count_documents({}) + 1
    time = datetime.now()
    order_dict["timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ")
    total_amount = 0
    for item in order_dict["items"]:
        item_doc = items_collection.find_one({"item_id": item["productId"]})
        if item_doc is None:
            raise HTTPException(status_code=404, detail="No item found.")
        if item_doc["quantity"] < item["boughtQuantity"]:
            raise HTTPException(status_code=400, detail="Not enough items in stock.")
        new_values = {
            "$set": {"quantity": item_doc["quantity"] - item["boughtQuantity"]}
        }
        items_collection.update_one({"item_id": item["productId"]}, new_values)
        total_amount += item_doc["price"] * item["boughtQuantity"]
    order_dict["total_amount"] = total_amount
    orders_collection.insert_one(order_dict)
    return individual_order_serial(order_dict)
