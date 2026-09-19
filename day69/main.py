from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor

# from flask_gravatar import Gravatar
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

# Import your forms from the forms.py
from forms import CreatePostForm, Registerform, Loginform, Commentform


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
loginmanager = LoginManager()
loginmanager.init_app(app)


@loginmanager.user_loader
def load_user(user_id):
    return db.get_or_404(Bloguser, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES


# TODO: Create a User table for all your registered users.
class Bloguser(UserMixin, db.Model):
    __tablename__ = "blogusers"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)
    comments = relationship("Comment", back_populates="comment_author")
    post = relationship("BlogPost", back_populates="author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blogusers.id"))
    author = relationship("Bloguser", back_populates="post")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # ***************Parent Relationship*************#
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blogusers.id"))
    comment_author = relationship("Bloguser", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
@login_required
def show_post(post_id):
    commentform = Commentform()
    requested_post = db.get_or_404(BlogPost, post_id)
    if request.method == "POST":
        commnet = Comment(
            text=commentform.body.data, #type:ignore
            author_id=current_user.id,  # from flask_login  #type:ignore
            post_id=post_id, #type:ignore
        )
        db.session.add(commnet)
        db.session.commit()
    result = db.session.execute(db.select(Comment).where(Comment.post_id == post_id))
    comments = result.scalars().all()
    return render_template("post.html", post=requested_post, form=commentform,commentlist=comments)


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route("/register", methods=["GET", "POST"])
def register():
    registerform = Registerform()
    if request.method == "POST":
        with app.app_context():
            email = registerform.email.data
            user = db.session.execute(
                db.select(Bloguser).where(Bloguser.email == registerform.email.data)
            ).scalar()
            if user:
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for("login"))
            hash_and_salted_password = generate_password_hash(
                request.form["password"], method="pbkdf2:sha256", salt_length=8
            )
            new_user = Bloguser(
                email=registerform.email.data, #type:ignore
                password=hash_and_salted_password, #type:ignore
                name=registerform.name.data, #type:ignore
            )
            db.session.add(new_user)
            db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=registerform)


# TODO: Retrieve a user from the database based on their email.
@app.route("/login", methods=["GET", "POST"])
def login():
    loginform = Loginform()
    if request.method == "POST":
        # print("form data sent and collected")
        result = db.session.execute(
            db.select(Bloguser).where(Bloguser.email == loginform.email.data)
        )
        user = result.scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, request.form["password"]):
            flash("Password incorrect, please try again.'")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("get_all_posts"))
    return render_template("login.html", form=loginform, current_user=current_user)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=request.form["title"], #type:ignore
            subtitle=request.form["subtitle"], #type:ignore
            body=request.form["body"], #type:ignore
            img_url=request.form["img_url"], #type:ignore
            author=current_user, #type:ignore
            date=date.today().strftime("%B %d, %Y"), #type:ignore
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = request.form["title"]
        post.subtitle = request.form["subtitle"]
        post.img_url = request.form["img_url"]
        post.author = current_user
        post.body = request.form["body"]
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# edit_form.title.data
# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
@login_required
def about():
    return render_template("about.html")


@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5050)


##Test Credentials
# Admin email: ajaykh053@gmail.com password : Blogposts@1234 username: Ajay
# Test email: test@gmail.com password: test@1234 username: Tester
