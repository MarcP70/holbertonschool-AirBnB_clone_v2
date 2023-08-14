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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Handle requests to the '/c/<text>' route and return a response with the modified text.

    Args:
        text (str): The text extracted from the URL path.

    Returns:
        str: The modified text with underscores replaced by spaces and prefixed with 'C'.
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
