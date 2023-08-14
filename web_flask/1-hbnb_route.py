#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Handle HTTP requests to the root URL ("/") of the Flask application
    and return a response.

    Returns:
        None

    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handle HTTP requests to the '/hbnb' URL and return a response of "HBNB".

    Returns:
        str: The string "HBNB" as the response to the HTTP request.
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
