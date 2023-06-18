print("Subscriber Python Script Started")

from kafka import KafkaConsumer
import json

kafka_bootstrap_servers = 'kafka:9092'
kafka_topic = 'x'

print("Kafka subscriber connecting")
try:
    consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_bootstrap_servers, value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    print("Kafka subscriber connected")
except Exception as e:
    print("Kafka subscriber error")
    exit(1)

for message in consumer:
    print(message.value)
