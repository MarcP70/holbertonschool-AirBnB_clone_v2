#!/usr/bin/python3
"""
Render the '10-hbnb_filters.html' template with all states and amenities.
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Render the '10-hbnb_filters.html' template with all states and amenities.

    Retrieves all states and amenities from the database
        using the `storage` object.
    Passes the retrieved states and amenities as arguments to the template.

    Returns:
        The rendered '10-hbnb_filters.html' template with states and amenities.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
