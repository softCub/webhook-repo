from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
mongo = os.getenv('MONGODB_URI')
#print(dir(pymongo))
client = MongoClient(mongo)
#print(client.list_database_names())
db = client.webhooks
#print(db.list_collection_names())
collections = db.events
#print(collections)
events =list( collections.find().sort("timestamp", -1).limit(5))
print(events)
