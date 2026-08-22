# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return (
#         '<h1 style="text-align: center">Hello, World</h1>'
#         '<div style="display:flex" ><p>Why are you gay</p> <br> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW4waXhvNDYwNzl2eWphMXNqcnIzY2VsOWw5dW42OWU5YmE3OGxueiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gb6TyakSW7F3mKx6VT/giphy.gif" style="width = 200 align-item:flex-start" > <p>Ur Gay</p> <br> <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTZxcDI1bXBsdDhoaTVzYXpmZTV0MnFiOWFjN2FteGxqN3d0b2NxaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gbwNUZEPU58BscyIqO/giphy.gif" style="width = 200 align-item:flex-end"></div>'
#     )


# def make_bold(fun):
#     def wrapper():
#         return "<b>" + fun() + "</b>"

#     return wrapper


# def make_emphasis(fun):
#     def wrapper():
#         return "<em>" + fun() + "</em>"

#     return wrapper


# def make_underlined(fun):
#     def wrapper():
#         return "<u>" + fun() + "</u>"

#     return wrapper


# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return "Bye"


# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello {name} you are {number} year old!"


# if __name__ == "__main__":
#     app.run(debug=True)


#Advance Decorators
# TODO: Create the logging_decorator() function 👇
def logging_decorator(fun):
    def wrapper(*args):
        print(f'You called a_function{(args)}\nIt returned {fun(*args)}')
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(4,5,6)