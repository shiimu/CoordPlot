import pickle
from flask import Flask, render_template, json, jsonify, redirect
import dbGet
import coordGet
import misc
import map
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map/")
def omap():
    return render_template('map.html')

@app.route('/Retcoords/')
def ret_C():
    coordGet.queryCoords()
    dbGet.findLast()
    from dbGet import last_coord
 
    return redirect("/")
@app.route('/clrgrp/')
def clear_Group():
    
    misc.dictClear()
    return redirect("/")

if __name__ == "__main__":
    app.run( debug = True )