class MessageManager:
    def __init__(self, consumer):
        self.consumer = consumer
        self.messages = []

    def run(self):
        for msg in self.consumer:
            self.messages.append(msg.value)  # שומר את ההודעה במשתנה
            # כאן תוכל גם לקרוא לפונקציות enrichment בהמשך
