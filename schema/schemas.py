# items
def individual_item_serial(item) -> dict:
    return {
        "item_id": item["item_id"],
        "name": item["name"],
        "price": item["price"],
        "quantity": item["quantity"]
    }

def multiple_item_serial(items) -> list:
    return [individual_item_serial(item) for item in items]

# orders
def individual_order_serial(order) -> dict:
    return {
        "timestamp": order["timestamp"],
        "items": multiple_unit_serial(order["items"]),
        "total_amount": order["total_amount"],
        "user_address": user_address_serial(order["user_address"])
    }

def multiple_order_serial(orders) -> list:
    return [individual_order_serial(order) for order in orders]

def individual_unit_serial(item) -> dict:
    return {
        "productId": item["productId"],
        "boughtQuantity": item["boughtQuantity"]
    }

def multiple_unit_serial(items) -> list:
    return [individual_unit_serial(item) for item in items]

def user_address_serial(address) -> dict:
    return {
        "city": address["city"],
        "country": address["country"],
        "zip_code": address["zip_code"]
    }