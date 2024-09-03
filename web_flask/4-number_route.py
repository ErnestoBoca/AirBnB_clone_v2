#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
