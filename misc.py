import pymongo
from pymongo.mongo_client import MongoClient
#Dictionary of retrieved coordinates

def coordDict():
    global coord_group
    coord_group = []

def dictClear():
    #coord_group.clear()
    #Also drop the collection and remake
    client = MongoClient('localhost', 27017)
    db = client['CoordsPlot']
    collection = db['coordinates']
    if collection.count() != 0:
        collection.drop()