from pymongo import MongoClient, collection
from coordGet import dumped_data

def addData():
    client = MongoClient('localhost', 27017)
    db = client['coordinates']
    collection = db['CoordPlot']
    collection.insert(dumped_data)