<<<<<<< HEAD
=======
#!/usr/bin/python3
>>>>>>> 5329b7a8c037230dd1ebb44320a6f419e9c25849
"""This script starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD

@app.route("/", strict_slashes=False)
def hello_route():
    """Prints Hello World"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
=======
@app.route("/", strict_slashes=False)
def hello_route():
	"""Prints Hello World"""
	return "Hello HBNB!"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
>>>>>>> 5329b7a8c037230dd1ebb44320a6f419e9c25849
