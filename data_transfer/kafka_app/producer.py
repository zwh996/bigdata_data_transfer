from kafka import KafkaProducer
import json
from data_transfer import settings


def kafka_producer_send_message(message):

    kafka_server = 'localhost:9092'

    # Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=kafka_server,
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )

    # send msg
    producer.send(settings.kafka_default_config["kafka"]["topic_name"], message)
    producer.flush()
