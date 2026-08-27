import os
os.close
import requests
from flask import Flask, render_template
# from post import Post
app = Flask(__name__)

respones = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route("/")
def home():
    return render_template("index.html", posts=respones)


@app.route("/post/<int:id>")
def get_post(id):
    return render_template("post.html", postid=id, post=respones)


if __name__ == "__main__":
    app.run(debug=True)
