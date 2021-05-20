from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from json import dumps
from bson.objectid import ObjectId
from bson.json_util import dumps
from pymongo.message import query

app = Flask("to-do-api")
app.config['MONGO_URI'] = 'mongodb://172.17.0.2:27017/to-do-app'

# PyMongo connects the flask to the mongoDB
database = PyMongo(app)
collection = database.db.tasks

# Schema includes the task and done bool to check for the task is done or not.

@app.route('/add_task', methods=['POST'])
def add_task():
    task_data = request.json
    print(task_data)
    # insert data
    collection.insert_one(task_data).inserted_id
    response = jsonify("Done")
    response.status_code = 201
    return response


@app.route('/tasks', methods=['GET'])
def show_tasks():
    documents = collection.find()
    response = jsonify(dumps(documents))
    response.status_code = 200
    return response


@app.route("/show_task/<id>", methods=['GET'])
def show_task(id):
    document = collection.find_one({'_id': ObjectId(id)})
    response = jsonify(dumps(document))
    response.status_code = 200
    return response


@app.route('/delete_one/<id>', methods=['DELETE'])
def delete_one(id):
    delete = collection.delete_one({'_id': ObjectId(id)})
    print(delete)
    response = jsonify("Deleted {} successfully".format(id))
    response.status_code = 200
    return response


@app.route('/delete_all', methods=['DELETE'])
def delete_all():
    delete = collection.delete_many({})
    print(delete)
    response = jsonify("Deleted all the tasks successfully")
    response.status_code = 204
    return response


@app.route('/update_task/<id>', methods=['PUT'])
def update_task(id):
    query = request.json
    print(query)
    task = query['task']
    done = query['done']
    if task and done and id and request.method == 'PUT':
        update = collection.update_one({'_id': ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)}, {
            '$set': {'task': task, 'class': done}})
        print(update)
        response = jsonify("Update Successful")
        response.status_code = 200
        return response

    else:
        return jsonify("Error")


app.run(port=5555, debug=True)
