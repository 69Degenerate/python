import pymongo

client = pymongo.MongoClient("mongodb+srv://vishal:root@cluster0.4g6eqfu.mongodb.net/?retryWrites=true&w=majority")
db = client.python.emp
print(db.find_one())
# data={
#   "empno": 2,
#   "ename": "1",
#   "job": "1",
#   "mgr": 121,
#   "hiredate": "10-10-99",
#   "sal": 1,
#   "comm": 1,
#   "deptno": 1
# }
# # db.insert_one(data)
# # print(db.find())
# for rec in db.find():
#     print(rec)