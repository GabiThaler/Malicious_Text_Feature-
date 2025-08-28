import json
from kafka import KafkaConsumer
from message_manager import MessageManager
from sentiment import SentimentProcessor
from enrich_handler import EnrichHandler
from weapon import WeaponProcessor
from producer import Producer

consumer = KafkaConsumer(
    'raw_tweets_antisemitic',
    bootstrap_servers='localhost:9092',
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
)
print('consumer started')

sp = SentimentProcessor()
wp = WeaponProcessor("./data/weapon_list.txt")
prod = Producer()

handler = EnrichHandler(
    sentiment_processor=sp,
    weapons_detector=wp,
    producer=prod,
    output_topic='enriched_preprocessed_tweets_antisemitic'
)

manager = MessageManager(consumer, handler)
manager.run()
