import gpxpy
from pymongo.mongo_client import MongoClient


def addGPXData():
    
    from dbGet import coordListLongt,coordListLatt

    gpx = gpxpy.gpx.GPX()

    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)
    for i,j in zip(coordListLongt, coordListLatt):
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(j, i))

#Trying to get it to work with a simple file before going into mongodb.
    print('Created GPX File:', gpx.to_xml())
    with open("locations.gpx", "w") as f:
        f.write(gpx.to_xml())
    #client = MongoClient('localhost', 27017)
    #db = client['CoordsPlot']
    #collection = db['gpxData']
    #collection.insert(gpx.to_xml())