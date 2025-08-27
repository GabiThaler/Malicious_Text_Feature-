#נצרך להסיר סחמני פיסוק
import re
import string
#נצרך לקבל קשימה של כל המילות חיבור
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


class Cleaner:
    def __init__(self,data):
        self.data=data
    #פונקציה שמנקה את הטקסט מסימני פיסוק
    def Removing_punctuation_marks(self,text):
        #פונקציה מובנת בפייתון שמנקה טקסטים מסימני פיסוק
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    # פונקציה להסרת סימני פיסוק ותווים מיוחדים
    def remove_special_characters(self,text):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return cleaned_text

    #מסירים רווחים מיותרים
    def Removing_unnecessary_whitespace_characters(self,text):
        clean_text = " ".join(text.split())
        return clean_text


    #ממירים את כל האותיות לאותיות קטנות
    def Converting_text_to_lowercase(self,text):
        clean_text = text.lower()
        return clean_text

    #מסיר את כל המילות חיבור
    def Removing_stop_words(self, text):
        words = text.split()
        filtered = [w for w in words if w.lower() not in ENGLISH_STOP_WORDS]
        return " ".join(filtered)





cc=Cleaner("gab#@!$@#i is "
           "#@!$%th!!~e     "
           "k$#ing")
a=cc.Removing_punctuation_marks("   GAb#@!$@#i is "
           "            #@!$%th!!~e     "
           "k$#iNg")
print(a)
a=cc.remove_special_characters(a)
print(a)
a=cc.Removing_unnecessary_whitespace_characters(a)
print(a)
a=cc.Converting_text_to_lowercase(a)
print(a)
a=cc.Removing_stop_words(a)
print(a)