# from os import uname
from pymongo import MongoClient
from flask import Flask,request,flash
from flask import render_template,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
con=MongoClient('mongodb://127.0.0.1:27017')
db=con['python']
coll=db['login']


    
@app.route("/", methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'):
        u = request.form.get('username')
        p = request.form.get('password')
        print(u,' ',p)
        s=coll.find_one({'uname':u,'pass':p})
        if s is None:
            print('no log')
            return render_template("log.html")
        else:
            print('log')
            return redirect("/home")
    else:
        return render_template("log.html")

@app.route("/create", methods = ['GET', 'POST'])
def create():
    if(request.method=='POST'):
        p = request.form.get('password')
        e = request.form.get('email')
        u = request.form.get('username')
        print(u,e,p)
        s=coll.find_one({'uname':u,'pass':p,'email':e})
        print(s)
        if s is None:
            print('no user found')
            coll.insert_one({'uname':u,'pass':p,'email':e})
            return redirect("/")
        else:
            print("username already exist")
            return render_template("create.html")
    else:
        return render_template("create.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)

