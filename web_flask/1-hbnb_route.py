#!/usr/bin/python3
"""web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display HBNB """

from flask import Flask
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hello():
    """  displays 'Hello HBNB!' """
    return "Hello HBNB!"


def hello_hbnb():
    """displays HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
