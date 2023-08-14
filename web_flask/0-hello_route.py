#!/usr/bin/env python3
"""
Starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Handle HTTP requests to the root URL ("/") and return a greeting message.

    Returns:
        str: A greeting message.

    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
