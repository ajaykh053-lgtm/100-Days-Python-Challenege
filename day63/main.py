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
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collectionday63.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars().all()
    # print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form["Bookname"],
                author=request.form["BookAuthor"],
                rating=request.form["Rating"],
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/Edit/<int:book_id>",methods=['GET','POST'])
def Edit(book_id):
    if request.method == "POST":
        with app.app_context():
            change_rating = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            print(change_rating)
            print(request.form['new_rating'])
            change_rating.rating = request.form['new_rating']
            db.session.commit()
        return redirect(url_for('index'))
    else :
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template('edit.html',books=all_books,book_id=book_id)

@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    with app.app_context():
        delete_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(delete_book)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
