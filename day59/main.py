from flask import Flask, url_for, render_template
from pprint import pprint
import requests

app = Flask(__name__)

Endpoint = "https://api.npoint.io/fff2c15cf4b2280f9863"
respones = requests.get(url=Endpoint).json()
# pprint(respones)


@app.route("/")
def home():
    blogs = respones
    # pprint(blogs)
    return render_template("index.html", posts=blogs)


@app.route("/index")
def index():
    blogs = respones
    return render_template("index.html",posts=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/posthtml/<int:id>")
def getpost(id):
    blogs=respones
    return render_template("post.html",blog_post=blogs,post_id=id)
if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=5000)
