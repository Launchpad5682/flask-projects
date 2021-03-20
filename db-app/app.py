from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("realapp")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'

# ORM
db = SQLAlchemy(app)


class IIEC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    remarks = db.Column(db.Text)

    def __init__(self, name, age, remarks):
        self.name = name
        self.age = age
        self.remarks = remarks


db.create_all()

# Create
"""
helm = IIEC('Saurabh', 20, 'OK')
db.session.add(helm)
db.session.commit()
"""


# Read
"""
hello = IIEC.query.get(2)
print(helm.name, helm.age, helm.remarks)
"""

# Update
"""
hell = IIEC.query.get(3)
print(hell.name, hell.age, hell.remarks)
hell.age = 27
db.session.add(hell)
db.session.commit()
"""

# Delete
"""
rall = IIEC.query.get(3)
db.session.delete(rall)
db.session.commit()
"""