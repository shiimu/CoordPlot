from flask import Flask, render_template, json, jsonify
from coordGet import queryCoords  
import pickle
import dbGet
app = Flask(__name__)


@app.route("/")
def index():
    queryCoords()
    from coordGet import data_const
    dbGet.getData()


    return pickle.dumps(data_const)

if __name__ == "__main__":
    app.run( debug = True )