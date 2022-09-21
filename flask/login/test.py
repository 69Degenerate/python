# from os import uname
from queue import Empty
from  flask import Flask,request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/postgres'
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
            return render_template("create.html")
    else:
        return render_template("log.html")

    
@app.route("/create", methods = ['GET', 'POST'])
def create():
    if(request.method=='POST'):
        p = request.form.get('password')
        e = request.form.get('email')
        u = request.form.get('username')
        print(u,e,p)
        s=db.session.execute(db.session.query(logs.uname,logs.pas).where(logs.uname==u,logs.email==e,logs.pas==p)).one_or_none()
        print(s)
        if s is None:
            print('no log')
            entry = logs(name=u,email = e,pas=p)
            db.session.add(entry)
            db.session.commit()
            return render_template("log.html")
        else:
            print('log')
            return render_template("create.html")
    else:
        return render_template("create.html")



app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True