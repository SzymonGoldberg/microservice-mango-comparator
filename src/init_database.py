import pymongo

init_data = [
    {"_id": 0, "string": "hello"},
    {"_id": 1, "string": "have a nice day"},
    {"_id": 2, "string": "nevermind"},
]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cold_database"]
collection = mydb["collection"]

collection.insert_many(init_data)
