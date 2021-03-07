from flask import Flask
from flask import render_template
from flask import request
import subprocess

app = Flask("realapp")


@app.route("/form")
def form():
    data = render_template("form.html")
    return data


@app.route("/result", methods=['GET'])
def result():
    cmd = request.args.get("x")
    output = subprocess.getoutput(cmd)
    return "<pre>" + output + "</pre>"
