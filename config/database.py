from pymongo.mongo_client import MongoClient


client=MongoClient("mongodb+srv://emailemailemail3439:57cj04K9gnnSKnfF@cluster0.n5rgghk.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

db=client.sample_db

items_collection = db["items_collection"]
orders_collection = db["orders_collection"]
