from flask import Flask, render_template, json, jsonify

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello"


if __name__ == "__main__":
    app.run( debug = True )