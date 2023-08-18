#!/usr/bin/python3
"""
This code snippet is a Flask application that defines a route for handling
requests related to states. It retrieves the states from the storage, and
based on the provided ID parameter, it either returns a specific state or
all states. The retrieved states are then passed to a template for rendering.
"""
# Import necessary modules
from models import storage
from models.state import State
from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# Define route for handling states requests


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """Retrieve all states from storage"""
    states = storage.all(State).values()
    if id is not None:
        # If ID is provided, find the matching state
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=state)
        # If no matching state is found, render template without passing
            # any state
        return render_template('9-states.html')
    # If no ID is provided, render template with all states
    return render_template('9-states.html', states=states, full=True)

# Define teardown function to close the storage


@app.teardown_appcontext
def teardown(self):
    """Closes the storage"""
    storage.close()


# Run the Flask application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
