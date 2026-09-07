# import sqlite3
# db = sqlite3.connect(database="books-collection.db")
# cursor = db.cursor()
# #Just run below code for first run and for next comment it out
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY UNIQUE, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# # )
# #Insert Values into the table in sqllite3,After intseting comment it out
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# # db.commit()
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
Bootstrap5(app=app)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collectionday63.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book:
    id: Mapped[int] = mapped_column(
        Integer, nullable=False, primary_key=True, unique=True
    )
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

all_books = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form["Bookname"],
                author=request.form["BookAuthor"],
                rating=request.form["Rating"],
            )
            db.session.add(new_book)
        with app.app_context():
            book_dict = {
                "title": f"{db.session.execute(db.select(Book).where(Book.title == request.form['Bookname'])).scalar()}",
                "author": f"{db.session.execute(db.select(Book).where(Book.title == request.form['BookAuthor'])).scalar()}",
                "rating": f"{db.session.execute(db.select(Book).where(Book.title == request.form['Rating'])).scalar()}",
            }
            all_books.append(book_dict)
    return render_template("index.html", all_books=all_books, heading="List is books")


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)