# from os import uname
from pymongo import MongoClient
from flask import Flask,request,flash
from flask import render_template,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'   
con=MongoClient('mongodb://127.0.0.1:27017')
db=con['python']
logcoll=db['login']
concoll=db['contact']



    
@app.route("/", methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'):
        u = request.form.get('username')
        p = request.form.get('password')
        print(u,' ',p)
        s=logcoll.find_one({'uname':u,'pass':p})
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
        s=logcoll.find_one({'uname':u,'pass':p,'email':e})
        print(s)
        if s is None:
            print('no user found')
            logcoll.insert_one({'uname':u,'pass':p,'email':e})
            return redirect("/")
        else:
            print("username already exist")
            return render_template("create.html")
    else:
        return render_template("create.html")
    
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/contact',methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        desc = request.form.get('desc')
        flash('massage sent')
        concoll.insert_one({
            'name':name,
            'email':email,
            'phone':phone,
            'desc':desc
        })
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template("about.html")

    
@app.route('/services')
def ser():
    return render_template("services.html")

if __name__=="__main__":
    app.run(debug=True)

