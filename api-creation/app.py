from flask import Flask, request, render_template, jsonify

app = Flask("iiec")

db = [
    {
        "id": 1,
        "name": "Saurabh",
        "email": "launchpad@gmail.com"
    },
    {
        "id": 2,
        "name": "Vimal",
        "email": "vimal@gmail.com"
    }
]

@app.route('/form')
def myform():
    return render_template("basic.html")


@app.route("/name/<y>")
def myname(y):
    return y.upper()


@app.route("/data", methods=["POST"])
def mydata():
    if request.method == 'POST':
        data = request.form.get("name")

    return data.upper()


@app.route("/spost", methods=["GET"])
def fun1():
    # return "GET request"
    return jsonify(db)


@app.route("/spost", methods=["PUT"])
def func2():
    return "PUT request"


@app.route("/spost", methods=["DELETE"])
def func3():
    return "DELETE request"

@app.route("/spost", methods=["POST"])
def func4():
    return "POST request"

app.run(port=5555, debug=True)