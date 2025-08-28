class EnrichHandler:
    def __init__(self, sentiment_processor, weapons_detector=None, producer=None, output_topic=None):
        self.sp = sentiment_processor
        self.wp = weapons_detector
        self.producer = producer
        self.output_topic = output_topic

    def handle(self, message: dict) -> dict:
        clean_text = message.get("clean_text", "")

        # enrich
        message["sentiment"] = self.sp.get_sentiment(clean_text)
        message["weapons_detected"] = self.wp.find_weapons(clean_text) if self.wp else []

        # publish (אם הוגדר)
        if self.producer and self.output_topic:
            key = message.get("id")  # לא חובה, שומר סדר per key
            self.producer.publish(self.output_topic, message, key=key)
        else:
            print(message)

        return message

