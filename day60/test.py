from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("test.html")


@app.route("/login", methods=["POST"])
def receive_data():
    return f"Name : {request.form['username']} Password : {request.form['password']}"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
