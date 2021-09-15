from flask import Flask, render_template, json, jsonify
from coordGet import queryCoords
app = Flask(__name__)


@app.route("/")
def index():
    queryCoords()
    return "Hello"

if __name__ == "__main__":
    app.run( debug = True )