import pymongo

client = pymongo.MongoClient("mongodb+srv://vishal:<password>@cluster0.4g6eqfu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)