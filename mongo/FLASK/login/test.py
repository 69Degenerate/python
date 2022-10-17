# from os import uname
from pymongo import MongoClient
from flask import Flask,request,flash
from flask import render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'   
con=MongoClient('mongodb://127.0.0.1:27017')
db=con['python']
logcoll=db['login']
concoll=db['contact']
demo=db['demo']

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


    
@app.route("/", methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'):
        u = request.form.get('username')
        p = request.form.get('password')
        print(u,' ',p)
        s=logcoll.find_one({'uname':u,'pass':p})
        if s is None:
            print('no log')
            flash('no user found')
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
            flash("user created")
            return redirect("/")
        else:
            print("username already exist")
            flash("username already exist")
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


@app.route('/services', methods=['GET'])
def face_upload_file():
     return render_template("services.html")

@app.route('/services/upload',methods=['POST'])
def face_upload():
    target = os.path.join(APP_ROOT, 'face-images/')  #folder path
    if not os.path.isdir(target):
            os.mkdir(target)     # create folder if not exits# database table name
    if request.method == 'POST':
        for upload in request.files.getlist("face_image"): #multiple image handel
            filename = secure_filename(upload.filename)
            destination = "/".join([target, filename])
            upload.save(destination)
            demo.insert_one({'face_image': filename})   #insert into database mongo db

        # return 
    return render_template("services.html")
   

if __name__=="__main__":
    app.run(debug=True)

