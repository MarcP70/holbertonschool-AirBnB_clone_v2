#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_or_state(id=None):
    """
    Handle requests for the "/states/" and "/states/<id>" endpoints.

    Retrieves all the State objects from the storage and renders a template
    with the states data.
    If an id is provided in the URL, it checks if there is a State object
    with that id and renders the template with the specific state data.

    Args:
        id (int, optional): The id of a specific state.

    Returns:
        str: Rendered HTML template with the states data (either all states
        or a specific state).
    """
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return render_template("9-states.html", states=state)
        return render_template("9-states.html")
    return render_template("9-states.html", states=states, full=True)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown the Flask application context.

    Args:
        exception: The exception raised, if any.
    """
    pass


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
