from flask import Flask ,jsonify ,request
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_DBNAME']='mansoor'
app.config['MONGO_URI']='mongodb://mansoor:mansoor@ds117858.mlab.com:17858/mansoor'

mongo=PyMongo(app)

@app.route("/form")
def index():
    students=[]
    # records = mongo.db.users.find({'name':'Hussain' or 'hussain','pass':'password'})
    records = mongo.db.users.find()
    for user in records:
        students.append({'name': user['name'], 'password': user['pass']})

    
    return jsonify({'SaylaniStudents': students})

@app.route("/add")
def add():
    add = mongo.db.users
    add.insert({'name' :'Sufiyan','pass':'Password'})
    return "Sucessfully add"
app.run(debug=True)