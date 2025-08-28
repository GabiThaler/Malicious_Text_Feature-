import json
from kafka import KafkaConsumer
from Enricher.message_manager import MessageManager
from Enricher.sentiment import SentimentProcessor
from Enricher.enrich_handler import EnrichHandler
from weapon import WeaponProcessor  # ← חדש

consumer = KafkaConsumer(
    'preprocessed_tweets_not_antisemitic',
    bootstrap_servers='localhost:9092',
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

sp = SentimentProcessor()
wp = WeaponProcessor("./data/weapon_list.txt")

handler = EnrichHandler(
    sentiment_processor=sp,
    weapons_detector=wp
)

manager = MessageManager(consumer, handler)
manager.run()
