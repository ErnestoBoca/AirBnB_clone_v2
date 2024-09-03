#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Prints Hello World"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Returns a text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Returns a text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """"Verify if is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Checks if the parameter is even or odd"""
    if n % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"
    return render_template("6-number_odd_or_even.html", n=n, number_type=number_type) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)