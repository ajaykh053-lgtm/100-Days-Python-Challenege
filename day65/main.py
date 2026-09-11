RESTapi = "REprentational state transfer"

restapi = "workflow --> Client + api + server + databse"

rulesforrestapi = "1.Use HTTP request verbs \
    2.Use specificc pattren of routes/endpoint url's"

# HTTP_VERBS = [GET,POST,PUT,PATCH,DELETE]
routeandemdpoint = "/elephant/giraff/hippos."
import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

app = Flask(__name__)
app.secret_key = "secretkeytocallthefroommaybe"


# CREATE DB
class Base(DeclarativeBase):
    pass


"8660709328"

# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


class CafeForm(FlaskForm):
    name = StringField("Cafe Name")
    map_url = StringField("Cafe Map URL")
    img_url = StringField("Cafe Image URL")
    location = StringField("Cafe Location")
    seats = StringField("Cafe Seats")
    has_toilet = BooleanField("Has Toilet (True/False)")
    has_wifi = BooleanField("Has Wifi (True/False)")
    has_sockets = BooleanField("Has Sockets (True/False)")
    can_take_calls = BooleanField("Can Take Calls (True/False)")
    coffee_price = StringField("Coffee Price")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/Getrandom")
def randomcafe():
    "In order to do this, we have to turn our random_cafe SQLAlchemy Object into a JSON. This process is called serialization."
    "Flask has a serialisation helper method built-in called jsonify() . But we have to provide the structure of the JSON to return."
    result = db.session.execute(db.select(Cafe.id).order_by(Cafe.id)).scalars().all()
    random_cafe = db.session.execute(
        db.select(Cafe).where(Cafe.id == random.choice(result))
    ).scalar()
    return jsonify(
        cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }
    )


@app.route("/Getall")
def allcafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    cafe_dict = {}
    for cafe in result:
        cafelist = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        # print(cafelist)
        cafe_dict[f"{cafe.id}"] = cafelist
    return jsonify(AllCafe=cafe_dict)


@app.route("/searchcafe/<location>")
def findcafe(location):
    locations = (
        db.session.execute(db.select(Cafe.location).order_by(Cafe.location))
        .scalars()
        .all()
    )
    if location in locations:
        result = (
            db.session.execute(db.select(Cafe).where(Cafe.location == location))
            .scalars()
            .all()
        )
        cafe_dict = {}
        for cafe in result:
            cafelist = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            }
            # print(cafelist)
            cafe_dict[f"{cafe.id}"] = cafelist
    else:
        cafe_dict = {
            "error": {"Not Found": "Sorry, we don't have a cafe at that location."}
        }
    return jsonify(AllCafe=cafe_dict)


# HTTP POST - Create Record
@app.route("/Post", methods=["GET"])
def cratecafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = Cafe(
            name=request.form["name"],
            map_url=request.form["map_url"],
            img_url=request.form["img_url"],
            location=request.form["location"],
            seats=request.form["seats"],
            has_toilet=request.form["has_toilet"],
            has_wifi=request.form["has_wifi"],
            has_sockets=request.form["has_sockets"],
            can_take_calls=request.form["can_take_calls"],
            coffee_price=request.form["coffee_price"],
        )
        db.session.add(cafe)
        db.session.commit()
    return ""


# HTTP PUT/PATCH - Update Record
@app.route("/Put/<name>")
def updatecafe(name):
    result = db.session.execute(db.select(Cafe).where(Cafe.name == name)).scalar()
    form = CafeForm()
    if form.validate_on_submit():
        result.name = (request.form["name"],)
        result.map_url = (request.form["map_url"],)
        result.img_url = (request.form["img_url"],)
        result.location = (request.form["location"],)
        result.seats = (request.form["seats"],)
        result.has_toilet = (request.form["has_toilet"],)
        result.has_wifi = (request.form["has_wifi"],)
        result.has_sockets = (request.form["has_sockets"],)
        result.can_take_calls = (request.form["can_take_calls"],)
        result.coffee_price = (request.form["coffee_price"],)
        db.session.commit()
    return ""


# HTTP DELETE - Delete Record
@app.route("/Delete/<name>")
def deletecafe(name):
    result = db.session.execute(db.select(Cafe).where(Cafe.name == name)).scalar()
    db.session.delete(result)
    db.session.commit()
    return ""


if __name__ == "__main__":
    app.run(debug=True)
