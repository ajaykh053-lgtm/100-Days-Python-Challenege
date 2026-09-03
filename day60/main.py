import requests
import smtplib
from flask import Flask, render_template,request

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/fff2c15cf4b2280f9863").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method == "POST":
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user="ajaykh052@gmail.com",password="jwjkarwdntvnrird")
        connection.sendmail(from_addr=request.form['email'],to_addrs="ajaykh053@gmail.com",msg=request.form['message'])
        return render_template("contact.html",heading="Successfully sent your message.")
    else:
        return render_template("contact.html",heading="Contact Me")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
