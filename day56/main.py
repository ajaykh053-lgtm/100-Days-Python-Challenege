from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inedx():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
# By typing this in console fo chrome we can direct edit website from the chrome
# document.body.contentEditable=true