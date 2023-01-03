# import demo
import requests
demoname='alll'
def test_read():
   res=requests.get("http://127.0.0.1:8000/read")
   return res.status_code==201

def test_readone():
   res=requests.get("http://127.0.0.1:8000/readone/30")
   return res.status_code==201

def test_readnama():
   res=requests.get("http://127.0.0.1:8000/readname/ward")
   return res.status_code==201

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
   return res.status_code==201

def test_demo_delete():
   url="http://127.0.0.1:8000/delete/"+demoname
   return requests.delete(url,timeout=1)

def test_update():
   res=requests.put