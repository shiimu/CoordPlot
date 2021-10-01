import re
from typing import MappingView
from pymongo import ALL, MongoClient
import pymongo
import os
import folium


global coordListLatt
global coordListLongt
coordListLongt = []
coordListLatt = []

def getData():
# Retrieve data from the database and sort in natural order and from the last added to the first. Must include
# major.inlatt and major.inglongt, dont show "_id"
    global last_coord
    client = MongoClient('localhost', 27017)
    db = client['CoordsPlot']
    collection = db['coordinates']
    last_coord = collection.find({}, {"major.inlatt" : 1 , "major.inlongt" : 1,'_id': False}).sort("$natural", pymongo.DESCENDING).limit(1)    
    sorting()

def sorting():
    # accessing latt and longt from the dictionary
    global longt
    global latt
    l = {}
    for x in (last_coord):
        l['sorted'] = x
    withoutS = l['sorted']    
    withoutM = withoutS['major']
    longt = withoutM['inlongt']
    latt = withoutM['inlatt']
    print(longt,latt)
    # Center map to the last coordinates retrieved
    import mapEmb
    mapEmb.centerLocation()
    toList()
    return longt, latt

def toList():
    # Add longt and latt to separate lists.
    coordListLongtAdd = coordListLongt.extend([longt])
    coordListLattAdd = coordListLatt.extend([latt])
    print(coordListLatt, coordListLongt )

def dictClear():
    #Drop the collection and delete locations.gpx
    client = MongoClient('localhost', 27017)
    db = client['CoordsPlot']
    collection = db['coordinates']
    if collection.count() != 0:
        collection.drop()
#Remove the gpx file as well    
    try:
        os.remove("locations.gpx")
    except:
        print('gpx file not found!')

#Default coordinates set to center on Helsinki. Its done to rewrite the map so the polylines dont show.
#Empty lonitude and lattitude lists.
    latt = "60.171944"
    longt = "24.941389"
    map1 = folium.Map(location=[latt, longt], zoom_start=8)
    map1.save("./templates/map.html")
    coordListLatt.clear()
    coordListLongt.clear()
