import random

from kafka import KafkaConsumer

print("Subscriber Python Script Started")

kafka_bootstrap_servers = 'kafka:9092'
kafka_topic = 'x'

print("Kafka subscriber connecting")
try:
    consumer = KafkaConsumer(
        kafka_topic,  # Kafka topic to consume from
        bootstrap_servers=kafka_bootstrap_servers,  # Kafka broker(s)
        group_id=str(random.Random(999999999)),  # Consumer group ID
        auto_offset_reset='latest',  # Start consuming from the latest offset
        enable_auto_commit=True,  # Enable automatic offset commits
        value_deserializer=lambda x: x.decode('utf-8')  # Deserialize message value as string
    )
    print("Kafka subscriber connected")
except Exception as e:
    print("Kafka subscriber error !!(Please Wait For Kafka To Start)!!")
    exit(1)

for message in consumer:
    print(message.value)
