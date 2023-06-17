from pymongo import MongoClient
import kafka
import json
import time
import random

mongodb_uri = "mongodb+srv://yusufagac:1233131@apachekafkacdcmongodb.ss1szsn.mongodb.net/?retryWrites=true&w=majority"
mongodb_client = MongoClient(mongodb_uri)
mongodb_db = mongodb_client['mydatabase']
mongodb_collection = mongodb_db['mycollection']

kafka_bootstrap_servers = 'kafka:29092'
kafka_topic = 'x'
kafka_producer = kafka.KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                                     value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_data_to_kafka(data):
    kafka_data = {"data": data["value"]}
    kafka_producer.send(kafka_topic, value=kafka_data)
    kafka_producer.flush()


def check_new_data_in_mongodb():
    print(mongodb_collection.count_documents({}))
    if mongodb_collection.count_documents({}) == 0:
        print("No data in MongoDB")
        return
    last_document = mongodb_collection.find_one({}, sort=[("_id", 1)])
    print(last_document["value"])
    last_document_id = last_document["_id"]
    while True:
        time.sleep(4)
        last_document = mongodb_collection.find({"_id": {"$gt": last_document_id}}).sort("_id", 1).limit(1)
        document_count = mongodb_collection.count_documents({"_id": {"$gt": last_document_id}})
        if document_count > 0:
            last_document_id = last_document[0]["_id"]
        else:
            continue
        print(last_document[0]["value"])
        send_data_to_kafka(last_document[0])

check_new_data_in_mongodb()
