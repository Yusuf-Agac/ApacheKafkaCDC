import os
import random
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# This file is for generating new test data for MongoDB
# This file is not used in docker you can run it on your local machine for generating new test data

uri = "mongodb+srv://" + "!!!YOUR_USERNAME!!!" + ":" + "!!!YOUR_PASSWORD!!!" + "@apachekafkacdcmongodb.ss1szsn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['kafkaDatabase']
collection = db['kafkaCollection']

if collection.count_documents({}) == 0:
    myDict = {"value": 0}
    inserted = collection.insert_one(myDict)
    last_document_id = inserted.inserted_id

last_document = collection.find_one({}, sort=[("value", -1)])
last_value = last_document["value"]

while True:
    last_value = last_value + 1
    myDict = {"value": last_value}
    print(myDict)
    inserted = collection.insert_one(myDict)
    time.sleep(2)
