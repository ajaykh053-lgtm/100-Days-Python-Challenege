from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = [
    {
        "title": "Harry Potter",
        "author": "J. K. Rowling",
        "rating": 9,
    },
    {
        "title": "Tail of two cities",
        "author": "Chalres Dickens",
        "rating": 7,
    }
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        book_dict = {
            'title' : f"{request.form['Bookname']}",
            'author' : f"{request.form['BookAuthor']}",
            'rating' : f"{request.form['Rating']}"
        }
        all_books.append(book_dict)
    return render_template("index.html",all_books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
