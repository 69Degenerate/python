from gc import collect
import pymongo
con=pymongo.MongoClient('mongodb://127.0.0.1:27017')
db=con['python']
col=db['demo']
d=col.find()
print(type(d))