#!/usr/bin/python3
"""web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display HBNB
/c/<text>: display “C ” followed by the value of the text variable
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """  displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_display():
    """ displays C followed by processed  value of txt """
    processed_text = text.replace("_", " ").capitalize()
    return f"C {processed_text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
