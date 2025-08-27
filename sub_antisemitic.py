import json
from message_manager import MessageManager
from kafka import KafkaConsumer


consumer = KafkaConsumer(
        'raw_tweets_antisemitic',
        bootstrap_servers='localhost:9092',
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

manager = MessageManager(consumer)
manager.run()