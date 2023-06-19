import os
from pymongo import MongoClient
import kafka
import json
import time

print("Producer Python Script Started")

# MongoDB connection
mongodb_uri = "mongodb+srv://" + os.environ.get("MONGODB_USERNAME") + ":" + os.environ.get("MONGODB_PASSWORD") + "@apachekafkacdcmongodb.ss1szsn.mongodb.net/?retryWrites=true&w=majority"
mongodb_client = MongoClient(mongodb_uri)
mongodb_db = mongodb_client['kafkaDatabase']
mongodb_collection = mongodb_db['kafkaCollection']

# Kafka connection
kafka_bootstrap_servers = 'kafka:9092'
kafka_topic = 'x'

print("Kafka producer connecting")
try:
    kafka_producer = kafka.KafkaProducer(
        bootstrap_servers=kafka_bootstrap_servers,  # Kafka broker(s)
        value_serializer=lambda x: json.dumps(x).encode('utf-8')  # Serialize message value as bytes
    )
    print("Kafka producer connected")
except Exception as e:
    print("Kafka producer error !!(Please Wait For Kafka To Start)!!")
    exit(1)


def send_data_to_kafka(data):
    kafka_data = {"message": data["value"]}
    print("Kafka Producer Sent: " + str(kafka_data))
    kafka_producer.send(kafka_topic, value=kafka_data)
    kafka_producer.flush()


# Check MongoDB for new data and send it to Kafka
def check_new_data_in_mongodb():
    print("MongoDB Count of Documents: " + str(mongodb_collection.count_documents({})))  # print number of documents in collection
    if mongodb_collection.count_documents({}) == 0:  # if collection is empty, insert a document
        mongodb_collection.insert_one({"value": 0})
    last_document = mongodb_collection.find_one({}, sort=[("_id", 1)])  # get the first document
    last_document_id = last_document["_id"]
    # check for new documents in collection
    while True:
        time.sleep(2)
        last_document = mongodb_collection.find({"_id": {"$gt": last_document_id}}).sort("_id", 1).limit(1)
        document_count = mongodb_collection.count_documents({"_id": {"$gt": last_document_id}})
        if document_count > 0:  # if there is a new document
            last_document_id = last_document[0]["_id"]
        else:
            continue
        send_data_to_kafka(last_document[0])  # send the new document to Kafka


check_new_data_in_mongodb()
