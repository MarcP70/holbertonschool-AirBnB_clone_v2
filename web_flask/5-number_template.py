#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template

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
    Handle requests to the '/c/<text>' route and return a response with
    the modified text.

    Args:
        text (str): The text extracted from the URL path.

    Returns:
        str: The modified text with underscores replaced by spaces and
        prefixed with 'C'.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is cool'):
    """
    Handle HTTP requests with the '/python/' endpoint and return a response
    based on the provided text parameter.

    Args:
        text (str, optional): The text to be displayed in the response.
        Defaults to 'is cool'.

    Returns:
        str: The HTTP response containing the provided or default text.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Handle HTTP requests with a specific route pattern '/number/<int:n>'
    and return a response containing the value of 'n' as a string along
    with the message "is a number".

    Args:
        n (int): The number to be included in the response message.

    Returns:
        str: A string response containing the value of 'n' and
        the message "is a number".
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """
    Render a template named '5-number.html' with the given number 'n' as
    a parameter.

    Args:
        n (int): The number to be passed as a parameter to the template.

    Returns:
        str: The rendered template with the provided number 'n'.
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
