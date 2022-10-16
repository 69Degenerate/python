# from crypt import methods
from flask import Flask,request,render_template
from pymongo import MongoClient
app=Flask(__name__)
con=MongoClient('mongodb://127.0.0.1:27017')
db=con['python']
coll=db['flask']

@app.route('/',methods=['GET','POST'])
def form():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        desc = request.form.get('desc')
        print(name,email,phone,desc)
        coll.insert_one({
            'name' :name,
            'email':email,
            'phone':phone,
            'desc' :desc
        })
    return render_template('contact.html')
app.run(debug=True)