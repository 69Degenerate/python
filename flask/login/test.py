# from os import uname
# from curses import flash
# from queue import Empty
from http.client import responses
from flask import Flask,request,flash
from flask import Response
from flask import render_template,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/postgres'
app.config['SECRET_KEY'] = 'the random string'   
db = SQLAlchemy(app)


class logs(db.Model):
    uname = db.Column(db.String(80), primary_key=True)
    pas = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
 
    
@app.route("/", methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'):
        u = request.form.get('username')
        p = request.form.get('password')
        print(u,' ',p)
        s=db.session.execute(db.session.query(logs.uname,logs.pas).where(logs.uname==u,logs.pas==p)).one_or_none()
        print(s)
        if s is None:
            print('no log')
            return render_template("log.html")
        else:
            print('log')
            # return render_template("create.html")
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
        s=db.session.execute(db.session.query(logs.uname).where(logs.uname==u)).one_or_none()
        print(s)
        if s is None:
            print('no user found')
            flash("user created")
            entry = logs(uname=u,email = e,pas=p)
            db.session.add(entry)
            db.session.commit()
            return redirect("/")
        else:
            print('no log')
            flash("username already exist")
            return render_template("create.html")
    else:
        return render_template("create.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)

