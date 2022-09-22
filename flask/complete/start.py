import imp
from  flask import Flask,request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import json

# app=Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/postgres'
db = SQLAlchemy(app)

class cont(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    no = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    # date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def index():
    return render_template("home.html")

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
        entry = cont(name=name, no = phone, msg = desc,email = email )
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template("about.html")

    
@app.route('/services')
def ser():
    return render_template("services.html")
app.run(host="0.0.0.0",port=80)


# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True
# app.config['TESTING'] = True
app.run(debug=True)