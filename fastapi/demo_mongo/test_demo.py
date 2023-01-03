import demo
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
demoname='alll'

def test_connection():
   client = demo.cli
   conn=True
   try:
      client.admin.command('ismaster')
   except ConnectionFailure:
      conn=False
   assert conn==True
   
   
def test_read():
   res=requests.get("http://127.0.0.1:8000/read")
   assert res.status_code==200


def test_readone():
   res=requests.get("http://127.0.0.1:8000/readone/30")
   assert res.status_code==200


def test_readnama():
   res=requests.get("http://127.0.0.1:8000/readname/ward")
   assert res.status_code==200


def test_items():
   url="http://127.0.0.1:8000/items/"
   data={
      "empno": 7499,
      "ename": demoname,
      "job": "salesman",
      "mgr": 7698,
      "hiredate": "20-02-81",
      "sal": 1600,
      "comm": 300,
      "deptno": 30
         }
   res=requests.post(url,data)
   assert res.status_code==200


def test_demo_delete():
   url="http://127.0.0.1:8000/delete/"+demoname
   res=requests.delete(url)
   assert res.status_code==200


def test_update():
   n="ward"
   res=requests.put("http://127.0.0.1:8000/update/?name="+n+"&newname="+n)
   assert res.status_code==200