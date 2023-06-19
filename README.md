# ApacheKafkaCDC


## Build and Run

To build and run the project, follow these steps:

1. Make sure you have Docker installed on your system.

2. Open docker-compose.yml then go to Services -> Producer -> Environment. You can replace your_username and your_password with the actual username and password you want to use for MongoDB. 
```yaml
environment:
  - MONGODB_USERNAME=example_username
  - MONGODB_PASSWORD=example_password
```

3. Open a terminal and navigate to the project directory.

4. Run the following **command** to start the project: `docker-compose up`


4. Wait for the services to start. Kafka takes a while to start up. You can check the logs to see if the services have started successfully.


## Description

The project consists of several components:

- **Zookeeper**: A centralized service for maintaining configuration information, naming, providing distributed synchronization, and group services for distributed systems.
- **Kafka**: A distributed streaming platform that allows you to publish and subscribe to streams of records.
- **Producer**: A Python script that connects to a MongoDB database and sends data to a Kafka topic.
- **Subscriber**: A Python script that consumes data from a Kafka topic.

The `docker-compose.yml` file defines the services required for the project. It sets up a Zookeeper instance, a Kafka instance, a producer instance, and multiple subscriber instances.

The `Producer.py` script establishes connections to both MongoDB and Kafka. It checks for new data in the MongoDB collection and sends it to the Kafka topic. The script uses the `kafka-python` library for interacting with Kafka.

The `Subscriber.py` script connects to the Kafka topic and consumes messages from it. It uses the `kafka-python` library for consuming Kafka messages.

Please refer to the source code for more details and configuration options.

## Architecture Diagram

![Architecture Diagram](images/general.png)

## Logs

### Producer Log

![Producer](images/Producer.png)

### Subscriber 1 Log

![Subs1](images/Subs1.png)

### Subscriber 2 Log

![Subs2](images/Subs2.png)

### Subscriber 3 Log

![Subs3](images/Subs3.png)