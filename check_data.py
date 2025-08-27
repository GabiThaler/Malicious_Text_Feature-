from dal import Dal
import pymongo
import time

class GetData:

    dal = Dal()
    collection = dal.open_connection()

    def get_collection(self):
        tweets = list()
        lenght = self.collection.count_documents({})
        current_jmp = 0
        try:
            while current_jmp < lenght:
                tweets += self.collection.find({}).limit(100).skip(current_jmp).sort('CreateDate', 1)
                current_jmp += 100
                time.sleep(60)
                print("sleep 60 second")
                
        except Exception as e:
            print(e)
        return tweets

a = GetData()

print(a.get_collection())