import os
import random
import requests
import datetime
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.date.today().year
    number = random.randint(1,19)
    return render_template("copyright.html",num=number,year=year)



@app.route("/<username>")
def index(username):
    gender_params = {
        "name": f"{username}",
        "country_id": "IN",
        "apikey": f"{os.environ['API']}",
    }
    age_params = {
        "name": f"{username}",
        "country_id": "IN",
        "apikey": f"{os.environ['API']}",
    }
    respones_gender = requests.get(
        url=os.environ["GENDER_ENDPOINT"], params=gender_params
    )
    respones_age = requests.get(url=os.environ["AGE_ENDPOINT"], params=age_params)
    return render_template(
        "names.html",
        name=username,
        gender=respones_gender.json()["gender"],
        age=respones_age.json()["age"],
    )

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    posts = requests.get(url=os.environ['BLOG_URL']).json()
    return render_template("blog.html",blogs=posts)

if __name__ == "__main__":
    app.run(debug=True)