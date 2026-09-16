from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app=app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        hash_and_salted_password = generate_password_hash(
            password=request.form["password"], method="pbkdf2:sha256", salt_length=8
        )
        with app.app_context():
            new_user = User(
                name=request.form["name"],
                email=request.form["email"],
                password=hash_and_salted_password,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            print("user registered")
            return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        with app.app_context():
            result = db.session.execute(db.select(User).where(User.email == email)).scalar()
            if not result:
                flash("That email does not exist, please try again.")
                return redirect(url_for('login'))
            elif not check_password_hash(result.password, password):
                flash('Password incorrect, please try again.')
                return redirect(url_for('login'))
            else:
                login_user(result)
                return redirect(url_for('secrets'))
    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route("/secrets")
@login_required
def secrets():
    # print(current_user.name)
    return render_template("secrets.html", user=current_user.name)

# @m87052833@1234
@app.route("/logout")
def logout():
    logout_user()
    print("user loged out")
    return redirect(url_for("login"))


@app.route("/download")
@login_required
def download():
    return send_from_directory(
        "static", path="files/cheat_sheet.pdf", as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
# " Example Email : ajaykh052@gmail.com Password : @Ajaykh@1234"