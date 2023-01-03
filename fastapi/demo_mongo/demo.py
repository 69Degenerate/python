from fastapi import FastAPI
import pymongo
app = FastAPI()
cli=pymongo.MongoClient("mongodb://localhost:27017")
db=cli.workdb.emp
@app.get("/")
def root():
    return {"name": "a"}


@app.get("/read")
def root():
    s=db.find({"deptno": 30},{'_id':False})
    print(s)
    di=[]
    for i in s:
        di.append(i)
    # print(di)
    # return di
    return di


@app.get("/readone/{m}")
async def readone(m):
    n=int(m)
    s=db.find({"deptno": n},{'_id':False})
    print(s)
    di=[]
    for i in s:
        di.append(i)
    print(type(n),n)
    print(di)
    # return di
    return di


@app.get('/readname/{name}')
def readname(name):
    s=db.find({"ename":{'$regex': name,'$options': 'i'}},{'_id':False})
    d=[]
    for i in s:
        d.append(i)
    return d


@app.post("/items/")
def insert():
    data={
    "empno": 7499,
    "ename": "allen",
    "job": "salesman",
    "mgr": 7698,
    "hiredate": "20-02-81",
    "sal": 1600,
    "comm": 300,
    "deptno": 30
  }
    db.insert_one({
    "empno": 7499,
    "ename": "allen",
    "job": "salesman",
    "mgr": 7698,
    "hiredate": "20-02-81",
    "sal": 1600,
    "comm": 300,
    "deptno": 30
  })
    return dict(data)

@app.delete('/delete/{name}')
def delete(name):
    db.delete_many({"ename":name})
    s=db.find({"deptno": name},{'_id':False})
    print(s)
    di=[]
    for i in s:
        di.append(i)
    return di


@app.put('/update/')
def update(name,newname):
    myquery = { "ename": { "$regex": name } }
    newvalues = { "$set": { "ename": newname } }
    x = db.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    s=db.find({"ename": newname},{'_id':False})
    print(s)
    di=[]
    for i in s:
        di.append(i)
    return di