# enrich_handler.py
class EnrichHandler:
    def __init__(self, sentiment_processor, weapons_detector=None, producer=None, output_topic=None):
        self.sp = sentiment_processor
        self.wp = weapons_detector
        self.producer = producer
        self.output_topic = output_topic

    def handle(self, message):
        if isinstance(message, list):
            for item in message:
                self._process_one(item)
            return message
        return self._process_one(message)

    def _process_one(self, msg: dict):
        if not isinstance(msg, dict):
            print(f"[EnrichHandler] Skipping non-dict message of type {type(msg)}")
            return msg

        clean_text = msg.get("clean_text", "")

        msg["sentiment"] = self.sp.get_sentiment(clean_text)

        if self.wp:
            if hasattr(self.wp, "find_weapons"):
                msg["weapons_detected"] = self.wp.find_weapons(clean_text) or []
            else:
                first = self.wp.find_weapon(clean_text)
                msg["weapons_detected"] = ([first] if first else [])
        else:
            msg["weapons_detected"] = msg.get("weapons_detected", [])

        if self.producer and self.output_topic:
            key = str(msg.get("id")) if msg.get("id") is not None else None
            self.producer.publish(self.output_topic, msg, key=key)
        else:
            print(msg)

        print(f"[enriched] id={msg.get('id')} sentiment={msg.get('sentiment')} weapons={msg.get('weapons_detected')}")
        return msg

