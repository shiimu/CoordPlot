from pymongo import ALL, MongoClient


def getData():
    client = MongoClient('localhost', 27017)
    db = client['coordinates']
    collection = db['CoordPlot']
    #query for latt and longtitude
    #global query_coords
    #query_coords = {"major.inlatt" : 1 , "major.inlongt" : 1}
    #for x in collection.find({} , {"major.inlatt" : 1 , "major.inlongt" : 1}):
    #    print(x)
#find_one should retrieve the latest one added if there are multiple matches.
    last_coord = collection.find_one({}, {"major.inlatt" : 1 , "major.inlongt" : 1})
    print(last_coord)