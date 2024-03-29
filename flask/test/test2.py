import imp
from  flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import json
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/contact')
def link():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

    
@app.route('/services')
def ser():
    return render_template("services.html")
app.run(host="0.0.0.0",port=80)


app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True