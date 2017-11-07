#!/usr/bin/python3
"""
Script to start a Flask web application and route to 3 pages for improv.live

For testing site locally.
"""

# Imports
from flask import Flask, render_template

# Create instance of Flask
app = Flask(__name__)

# Set strict_slashes for all routes
app.url_map.strict_slashes = False

@app.route('/')
@app.route('/index')
def index():
    """
    Method to render the index page
    """
    return render_template("index.html")

@app.route('/game')
def game():
    """
    Method to render the game page
    """
    return render_template("game.html")

@app.route('/wheel')
def wheel():
    """
    Method to render the wheel page
    """
    return render_template("wheel.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
