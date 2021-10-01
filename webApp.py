from flask import Flask, render_template, json, jsonify, redirect
import dbGet
import coordGet
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
#map.html for embedding into index.html
@app.route("/map/")
def omap():
    return render_template('map.html')

@app.route('/Retcoords/')
def ret_C():   
#redirects to homepage and initiates code for retrieve coordinates button
    coordGet.queryCoords()
    dbGet.getData()
    return redirect("/")

#redirects to homepage and initiates code for the save to gpx and plot button
@app.route('/saveGpx/')
def save_Gpx():
    import gpxMake
    gpxMake.addGPXData()
    return redirect("/")
#redirects to homepage and initiates code for the clear map button
@app.route('/clrgrp/')
def clear_Group():
    dbGet.dictClear()
    return redirect("/")

if __name__ == "__main__":
    app.run( debug = True )