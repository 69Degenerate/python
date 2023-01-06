
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://127.0.0.1:5500/calculator.html"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
num=[]
other=[]
table = soup.findAll(type='button')
for i in table:
    try:
        val=i['value']
        if isinstance(int(val),int):
            # print(val)
            num.append(i)
    except:
        other.append(i)
        pass

