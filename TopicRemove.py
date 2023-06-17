from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer

kafka_bootstrap_servers = 'localhost:29092'
kafka_topic = 'X'

# Create a KafkaAdminClient instance
admin_client = KafkaAdminClient(bootstrap_servers=kafka_bootstrap_servers)

# Create a list of topics to remove
topics_to_remove = [kafka_topic]

# Delete the topic
admin_client.delete_topics(topics_to_remove)

# Close the admin client
admin_client.close()
