from kafka import KafkaConsumer
import json

kafka_bootstrap_servers = 'localhost:29092'
kafka_topic = 'x'

consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_bootstrap_servers, value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for message in consumer:
    print(message.value)
