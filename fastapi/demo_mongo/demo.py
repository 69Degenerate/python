from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pymongo
from bson.json_util import dumps,loads
app = FastAPI()
cli=pymongo.MongoClient("mongodb://mongo:hKkb23G8NtWIezPQe4Cg@containers-us-west-197.railway.app:7613")
db=cli.workdb.emp
tem = Jinja2Templates(directory="./templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return tem.TemplateResponse("home.html", {"request": request})

@app.get("/read")
def read():
    s=db.find({"deptno": 30},{'_id':False})
    print(s)
    di = loads(dumps(list(s)))
    return di


@app.get("/readone/{deptno}")
async def readone(deptno):
    n=int(deptno)
    return loads(dumps(list(db.find({"deptno": n},{'_id':False}))))


@app.get('/readname/{ename}')
def readname(ename):
    return loads(dumps(list(db.find({"ename":{'$regex': ename,'$options': 'i'}},{'_id':False}))))


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
    db.insert_one(data)
    return dict(data)

@app.delete('/delete/{name}')
def delete(name):
    db.delete_many({"ename":name})
    s=db.find({"deptno": name},{'_id':False})
    return loads(dumps(list(s)))


@app.put('/update/')
def update(name,newname):
    myquery = { "ename": { "$regex": name } }
    newvalues = { "$set": { "ename": newname } }
    x = db.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    s=db.find({"ename": newname},{'_id':False})
    print(s)
    return loads(dumps(list(s)))