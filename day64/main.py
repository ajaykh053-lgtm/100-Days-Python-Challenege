from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movies_day64.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app=app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()
    db.session.commit()
#CREATE FROM
class movie(FlaskForm):
    title = StringField("Movie title",validators=[DataRequired()])
    rating = FloatField("Movie rating",validators=[DataRequired()])
    submit = SubmitField("Add")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/edit")
def editmovie():
    movies_form = movie()
    return render_template("edit.html",form=movies_form)


@app.route("/add")
def addmovie():
    return render_template("add.html")


@app.route("/delete")
def deletemovie():
    return render_template("index.html")


@app.route("/select")
def selectmovie():
    return render_template("select.html")


if __name__ == "__main__":
    app.run(debug=True)
