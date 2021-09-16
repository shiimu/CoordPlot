from flask import Flask, render_template, json, jsonify
from coordGet import queryCoords  
import pickle
import dbGet
import coordGet
app = Flask(__name__)


@app.route("/")
def index():
    queryCoords()
    from coordGet import dumped_data
    dbGet.getData()


    return pickle.dumps(dumped_data)

if __name__ == "__main__":
    app.run( debug = True )