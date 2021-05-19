from pymongo import MongoClient, cursor

# forming client connection with MongoDB
client = MongoClient("mongodb://172.17.0.2:27017/")

# creating or selecting a database


def db(client, db_name):
    database = client[db_name]
    return database

# creating or selecting a collection


def col(database, col_name):
    collection = database['contacts']
    return collection

# read a single document


def read_one(collection, query):
    document = collection.find_one(query)
    return document

# read the whole collection


def read_all(collection):
    cursor = collection.find({})
    for doc in cursor:
        print(doc)

    return None

# create single document


def insert_one(collection, document):
    doc_id = collection.insert_one(document).inserted_id
    return doc_id

# create multiple documents


def insert_many(collection, documents):
    documents = collection.insert_many(documents).inserted_id
    return documents

# update the documents


def update_one(collection, query, newValue):
    document = collection.update_one(query, newValue)
    return None

# delete the documents


def delete_one(collection, query):
    delete = collection.delete_one(query)
    return delete

# delete all the documents


def delete_all(collection):
    delete_all = collection.delete_many({})
    return delete_all.deleted_count
