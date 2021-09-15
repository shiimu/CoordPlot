import requests
import json
import pickle
# Get random coords from https://api.3geonames.org/?randomland=yes <- yes for random.  https://api.3geonames.org/randomland.FI Fi for finnish location
# 
def queryCoords():
    
    url = 'https://api.3geonames.org/randomland.FI.json'
    response = requests.request('GET', url,)
    dumped_data = response.json()
#Test data
    print(dumped_data)
