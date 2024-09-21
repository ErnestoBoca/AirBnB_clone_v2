#!/usr/bin/python3
"""This script fetches data from the database and prints on the screen"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """prints the states"""
    states = sorted(list(storage.all("State").values()),
                    key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """Prints the cities by the State"""
    states = sorted(list(storage.all("State").values()),
                    key=lambda x: x.name)
    for state in states:
        state.cities = sorted(list(state.cities), key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(exception):
    """removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")