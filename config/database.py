"""
This code connects to MongoDB Atlas using the provided connection string.
It then accesses the sample_db database and the items_collection and orders_collection collections within it.
"""
from pymongo.mongo_client import MongoClient

# Connect to MongoDB Atlas using the connection string
client = MongoClient(
    "mongodb+srv://emailemailemail3439:57cj04K9gnnSKnfF@cluster0.n5rgghk.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
)

# Access the sample_db database
db = client.sample_db

# Access the items_collection and orders_collection collections
items_collection = db["items_collection"]
orders_collection = db["orders_collection"]
