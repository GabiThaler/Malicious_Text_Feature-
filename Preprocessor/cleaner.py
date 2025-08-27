import string


class Cleaner:
    def __init__(self,data):
        self.data=data


    def Removing_punctuation_marks(self,text):
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

