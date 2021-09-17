from pymongo import ALL, MongoClient
import misc

global last_coord
last_coord = []
def getData():
    client = MongoClient('localhost', 27017)
    db = client['CoordsPlot']
    collection = db['coordinates']
    #query for latt and longtitude
    #global query_coords
    #query_coords = {"major.inlatt" : 1 , "major.inlongt" : 1}
    #for x in collection.find({} , {"major.inlatt" : 1 , "major.inlongt" : 1}):
    #    print(x)
#find_one should retrieve the latest one added if there are multiple matches.
    last_coord = collection.find_one({}, {"major.inlatt" : 1 , "major.inlongt" : 1})
    #print(type(last_coord))
def findLast():
    
    client = MongoClient('localhost', 27017)
    db = client['CoordsPlot']
    collection = db['coordinates']
    last_coord = collection.find({}, {"major.inlatt" : 1 , "major.inlongt" : 1}).sort("$natural", pymongo.DESCENDING).limit(1)
    for x in last_coord:
        print((x))

def addToDict():
    #From retrieved and sorted add to dictionary coordGroup[] 
    #print(coordGroup)
    return