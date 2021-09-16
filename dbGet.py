from pymongo import ALL, MongoClient


def getData():
    client = MongoClient('localhost', 27017)
    db = client['coordinates']
    collection = db['CoordPlot']
    #query for latt and longtitude
    
    for x in collection.find({} , {"major.inlatt" : 1 , "major.inlongt" : 1}):
        print(x)
        