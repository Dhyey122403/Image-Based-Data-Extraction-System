from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection URI
uri = "mongodb+srv://RaspberryPiModel4:DalBattiChurma@cluster0.0r1lp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB client
client = MongoClient(uri, server_api=ServerApi('1'))

# Select database and collection
db = client["EntityDatabase"]
collection = db["EntityCollection"]

# Function to insert entity data into MongoDB
def insert_entity_to_mongo(entity_name, entity_value):
    if entity_value is not None:
        document = {"entity_name": entity_name, "entity_value": entity_value}
        collection.insert_one(document)
        print(f"Inserted {entity_name}: {entity_value} into MongoDB")
    else:
        print(f"No value found for {entity_name}, nothing to insert.")
