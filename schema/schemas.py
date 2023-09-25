"""This module contains the schemas for the API."""


def individual_item_serial(item) -> dict:
    """Serializes an individual item.

    Args:
        item (dict): The item to be serialized.

    Returns:
        dict: The serialized item with the following keys:
            - item_id (str): The ID of the item.
            - name (str): The name of the item.
            - price (float): The price of the item.
            - quantity (int): The quantity of the item."""
    return {
        "item_id": item["item_id"],
        "name": item["name"],
        "price": item["price"],
        "quantity": item["quantity"],
    }


def multiple_item_serial(items) -> list:
    """Serializes a list of items.

    Args:
        items (list): The list of items to be serialized.

    Returns:
        list: The serialized items, where each item is a dictionary with the following keys:
            - item_id (str): The ID of the item.
            - name (str): The name of the item.
            - price (float): The price of the item.
            - quantity (int): The quantity of the item."""
    return [individual_item_serial(item) for item in items]


def individual_order_serial(order) -> dict:
    """Serializes an individual order.

    Args:
        order (dict): The order to be serialized.

    Returns:
        dict: The serialized order with the following keys:
            - order_id (str): The ID of the order.
            - timestamp (str): The timestamp of the order.
            - items (list): The serialized items in the order.
            - total_amount (float): The total amount of the order.
            - user_address (dict): The serialized user address."""
    return {
        "order_id": order["order_id"],
        "timestamp": order["timestamp"],
        "items": multiple_unit_serial(order["items"]),
        "total_amount": order["total_amount"],
        "user_address": user_address_serial(order["user_address"]),
    }


def multiple_order_serial(orders) -> list:
    """Serializes a list of orders.

    Args:
        orders (list): The list of orders to be serialized.

    Returns:
        list: The serialized orders, where each order is a dictionary with the following keys:
            - order_id (str): The ID of the order.
            - timestamp (str): The timestamp of the order.
            - items (list): The serialized items in the order.
            - total_amount (float): The total amount of the order.
            - user_address (dict): The serialized user address."""
    return [individual_order_serial(order) for order in orders]


def individual_unit_serial(item) -> dict:
    """Serializes an individual unit.

    Args:
        item (dict): The unit to be serialized.

    Returns:
        dict: The serialized unit with the following keys:
            - productId (str): The ID of the product.
            - boughtQuantity (int): The quantity of the product bought."""
    return {"productId": item["productId"], "boughtQuantity": item["boughtQuantity"]}


def multiple_unit_serial(items) -> list:
    """Serializes a list of units.

    Args:
        items (list): The list of units to be serialized.

    Returns:
        list: The serialized units, where each unit is a dictionary with the following keys:
            - productId (str): The ID of the product.
            - boughtQuantity (int): The quantity of the product bought."""
    return [individual_unit_serial(item) for item in items]


def user_address_serial(address) -> dict:
    """Serializes a user address.

    Args:
        address (dict): The user address to be serialized.

    Returns:
        dict: The serialized user address with the following keys:
            - city (str): The city of the address.
            - country (str): The country of the address.
            - zip_code (str): The zip code of the address."""
    return {
        "city": address["city"],
        "country": address["country"],
        "zip_code": address["zip_code"],
    }
