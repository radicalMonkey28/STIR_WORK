import pymongo
import time
import uuid

# Store trending topics in MongoDB
def store_in_mongodb(trending_topics, proxy_ip):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["twitter_data"]
    collection = db["trending"]

    unique_id = str(uuid.uuid4())
    data = {
        "_id": unique_id,
        "trending_topics": trending_topics,
        "date_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "proxy_ip": proxy_ip,
    }

    collection.insert_one(data)
    return data
