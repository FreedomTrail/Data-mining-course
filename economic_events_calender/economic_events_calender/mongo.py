import pymongo
from economic_events_calender.config import MONGO_URL


client = pymongo.MongoClient(MONGO_URL)


eec = client["eec"]
cl = eec["cl"]


if __name__ == "__main__":
    cl.create_index([("data", pymongo.ASCENDING)], background=True)

