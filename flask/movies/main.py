# import imp
from flask import Flask,render_template,request
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'   
c = MongoClient("mongodb+srv://vishal:root@cluster0.4g6eqfu.mongodb.net/?retryWrites=true&w=majority")
data=c.db.movieinfo

@app.route("/")
def home():
    info=data.find()
    return render_template('home.html',info=info)


@app.route("/search",methods = ['GET', 'POST'])
def search():
    if(request.method=='POST'):
        name=request.form.get('name')
    print(name)
    info=data.find({'name':{'$regex': name,'$options': 'i'}})
    print(info)
    return render_template('home.html',info=info)

@app.route("/download/<string:id>")
def download(id=''):
    print(id)
    rec=data.find_one({'name':id})
    return render_template('download.html',rec=rec)

app.run(debug=True)