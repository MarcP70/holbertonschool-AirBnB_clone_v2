#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Retrieve all states from the database, sort them alphabetically by name,
    and render a template with the states and their associated cities.

    Returns:
        str: Rendered template with states and cities.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """
    Closes the session used by the Flask application.

    :param exception: The exception that occurred during the teardown process,
        if any.
    :return: None
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
