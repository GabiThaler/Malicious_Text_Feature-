import cleaner


class Manager:
    def __init__(self):
        pass

    def clean(self,data):
        clean=cleaner.Cleaner()
        for message in data:
            text=message["text"]
            text = clean.Removing_stop_words(text)
            text = clean.Remove_special_characters(text)
            text = clean.Removing_unnecessary_whitespace_characters(text)
            text = clean.Converting_text_to_lowercase(text)
            text = clean.Removing_stop_words(text)
            text = clean.Lemtization(text)

            message["clean text"] = text






