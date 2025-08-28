class EnrichHandler:
    def __init__(self, sentiment_processor, weapons_detector=None):
        self.sp = sentiment_processor
        self.wp = weapons_detector

    def handle(self, message: dict) -> dict:
        clean_text = message.get("clean_text", "")

        message["sentiment"] = self.sp.get_sentiment(clean_text)

        if self.wp:
            message["weapons_detected"] = self.wp.find_weapon(clean_text)
        print(message)
        return message
