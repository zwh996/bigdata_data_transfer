import threading
from kafka import KafkaConsumer
import json
from data_transfer import settings

messages_list = []


def get_messages():
    res = messages_list.copy()
    messages_list.clear()
    return res


class KafkaConsumerThread(threading.Thread):
    def __init__(self, max_messages=5):
        threading.Thread.__init__(self)
        self.max_messages = max_messages
        self.message_count = 0

    def run(self):
        # Kafka服务器地址
        kafka_server = 'localhost:9092'

        # 创建一个Kafka消费者，用于接收消息
        consumer = KafkaConsumer(
            settings.kafka_default_config["kafka"]["topic_name"],
            group_id=settings.kafka_default_config["kafka"]["consumer_group"],
            bootstrap_servers=kafka_server,
            auto_offset_reset='earliest',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

        try:
            for message in consumer:
                print(f"Received message: {message.value}")
                messages_list.append(message.value)
                self.message_count += 1
                consumer.commit()
                if self.message_count >= self.max_messages:
                    break  # 达到消息限制，退出循环
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            consumer.close()
            print("Consumer closed.")
