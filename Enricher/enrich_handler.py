class EnrichHandler:
    def __init__(self, sentiment_processor, weapons_detector):
        if weapons_detector is None:
            raise ValueError("weapons_detector is required")
        self.sp = sentiment_processor
        self.wp = weapons_detector

    def handle(self, message: dict) -> dict:
        clean_text = message.get("clean_text", "")
        message["sentiment"] = self.sp.get_sentiment(clean_text)

        message["weapons_detected"] = self.wp.find_weapon(clean_text) or ""
        print(message)
        return message