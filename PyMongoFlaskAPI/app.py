from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from json import dumps
import json
from bson import objectid
from json import JSONEncoder

app = Flask("to-do-api")
app.config['MONGO_URI'] = 'mongodb://172.17.0.2:27017/to-do-app'

# PyMongo connects the flask to the mongoDB
database = PyMongo(app)
collection = database.db.tasks


def read_one(collection, query):
    doc_id = collection.find_one(query)
    return doc_id


@app.route('/add_task', methods=['POST'])
def add_task():
    task_data = request.json
    print(task_data)
    # insert data
    collection.insert_one(task_data).inserted_id
    return "Done", 201


@app.route('/tasks', methods=['GET'])
def show_tasks():
    tasks = []
    documents = collection.find()
    #list_document = list(documents)
    #json_tasks = dumps(list_document)
    # print(json_tasks)
    #test = jsonify({"tasks":tasks})
    for document in documents:
        doc = {'name': document['name'], 'class': document['class']}
        tasks.append(doc)
        #tasks.append(json.encode(document, cls=JSONEncoder))

    #print(tasks)
    return jsonify(tasks)


@app.route('/delete_one', methods=['DELETE'])
def delete_one():
    task = request.json
    print(task)
    delete = collection.delete_one(task)
    print(delete)
    return "Deleted", 204

@app.route('/delete_all', methods=['DELETE'])
def delete_all():
    delete = collection.delete_many({})
    print(delete)
    return "Deleted all",204

@app.route('/update_task', methods=['PUT'])
def update_task():
    return None

app.run(port=5555, debug=True)
