import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
        'raw_tweets_antisemitic',
        bootstrap_servers='localhost:9092',
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )