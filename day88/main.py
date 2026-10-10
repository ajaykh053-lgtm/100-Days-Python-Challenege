import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C"
Bootstrap5(app)

db = sqlite3.connect("instance/cafesday88.db", check_same_thread=False)


class Add_cafe_form(FlaskForm):
    name = StringField(label="name", validators=[DataRequired()])
    map_url = StringField(label="map_url", validators=[DataRequired(), URL()])
    img_url = StringField(label="img_url", validators=[DataRequired(), URL()])
    location = StringField(label="location", validators=[DataRequired()])
    has_sockets = BooleanField(label="has_sockets", validators=[DataRequired()])
    has_toilet = BooleanField(label="has_toilet", validators=[DataRequired()])
    has_wifi = BooleanField(label="has_wifi", validators=[DataRequired()])
    can_take_calls = BooleanField(label="can_take_calls", validators=[DataRequired()])
    seats = StringField(label="seats", validators=[DataRequired()])
    coffee_price = StringField(label="coffee_price", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cafes", methods=["GET", "POST"])
def cafes():
    cafe = db.execute("SELECT * FROM cafe").fetchall()
    heading = [
        description[0] for description in db.execute("SELECT * FROM cafe").description
    ]
    return render_template(
        "cafes.html",
        header_columns=heading,
        cafes=cafe,
    )


@app.route("/add_new_cafe", methods=["GET", "POST"])
def add_cafe():
    form = Add_cafe_form()
    if request.method == "POST":
        table = db.execute("SELECT * FROM cafe")
        table.execute(
            "INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                form.name.data,
                form.map_url.data,
                form.img_url.data,
                form.location.data,
                form.has_sockets.data,
                form.has_toilet.data,
                form.has_wifi.data,
                form.can_take_calls.data,
                form.seats.data,
                form.coffee_price.data,
            ),
        )
        db.commit()
    return render_template("add_cafe.html", form=form)


if __name__ == "__main__":
    app.run(host="localhost", port=3030, debug=True)
    # print(db.execute("SELECT * FROM CAFE").fetchall())
