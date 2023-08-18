#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=state)
        return render_template('9-states.html')
    return render_template('9-states.html', states=states, full=True)

@app.teardown_appcontext
def teardown(self):
    """Closes the storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
