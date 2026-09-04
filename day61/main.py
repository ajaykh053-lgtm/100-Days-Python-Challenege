from flask import Flask, render_template

##Creating forms with the help of the flask
from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError


def my_length_check(form, password):
    if len(password.data) < 8:
        raise ValidationError("Field must be more than or equal to 8 characters")


# use if you want custom validation things
# def Email_check(form, email):
#     if "@" not in email.data:
#         if "." not in email.data:
#             raise ValidationError("Invalid email")


class MyForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), my_length_check])
    submit = SubmitField("Log In")


app = Flask(__name__)
app.secret_key = "CreatingForm"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5002, host="localhost")
