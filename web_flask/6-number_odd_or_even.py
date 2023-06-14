#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
# Create a flask instamce
app = Flask(__name__)


# Create a route decorator
@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    if "_" in text:
        text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_text(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            number_type = 'even'
        else:
            number_type = 'odd'
    return render_template("6-number_odd_or_even.html", n=n,
            number_type=number_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
