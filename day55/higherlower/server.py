from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<h2> write in url after the / eg:(url/your number) </h2>"
        '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGJnOGVqdTZld2VkdzJhaHI2ZWwyMmN1ZXFxZ2d4c3h1YTZhaWxwbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RVCJ3vwebUGDpoy7Tm/giphy.gif" y>'
    )


@app.route("/<int:userguess>")
def user_number(userguess):
    number = randint(0, 9999)
    if userguess < number:
        return (
            "<h3>Fhaaaaaa you suck its too lowwwwww !</h3"
            "<h3>Guess again ?</h3>"
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXN4MjM0cmZwcnVnb2RjZHZ6ZzE3cGhudDRhZjJ5d3IzbnNtajJ2bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Iy1PWGPb7Hz3AI4e3T/giphy.gif" y>'
        )
    elif userguess > number:
        return (
            "<h3>Fhaaaaaa you suck its too highhh !</h3"
            "<h3>Guess again ?</h3>"
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzViZGg5dWxraDd2MXJrOWVvN3ZqNW1nNzE0ZTQ1YXEycTY3ZTJybCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0SVAVxeJsnJ1WRMIPX/giphy.gif" >'
        )
    else:
        return (
            "<h3>All the best for next time. </h3"
            "<h3>Guess again ?</h3>"
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2k5bzNoeHB1N3UzdDBqZ3l2Y3V0eGNuNXJlNmFyNzk0YnRkdHJlYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YSD04aQmVadOQen7rH/giphy.gif" >'
        )


if __name__ == "__main__":
    app.run(debug=True)