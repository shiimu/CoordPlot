import requests
from pymongo import MongoClient, collection

# Get random coords from https://api.3geonames.org/?randomland=yes <- yes for random.  https://api.3geonames.org/randomland.FI Fi for finnish location
# 
def queryCoords():
    global dumped_data
    url = 'https://api.3geonames.org/?randomland=FI&json=1'
    response = requests.request('GET', url,)
    dumped_data = response.json()
    
#Test data
    #print(dumped_data)
    addData()
    print("data queried and added to the database")
def addData():
    client = MongoClient('localhost', 27017)
    db = client['CoordsPlot']
    collection = db['coordinates']
    collection.insert(dumped_data)
