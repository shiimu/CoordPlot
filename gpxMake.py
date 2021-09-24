import gpxpy
from pymongo.mongo_client import MongoClient
import folium
import os

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
    drawGpx()
    #client = MongoClient('localhost', 27017)
    #db = client['CoordsPlot']
    #collection = db['gpxData']
    #collection.insert(gpx.to_xml())
def drawGpx():
    gpx_file = open('C:\Github\CoordPlot\locations.gpx', 'r')
 
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    print(points)
    ave_lat = sum(p[0] for p in points)/len(points)
    ave_lon = sum(p[1] for p in points)/len(points)
 
# Load map centred on average coordinates
    my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=8)
 
#add a markers
    for each in points:  
        folium.Marker(each).add_to(my_map)
 
#fadd lines
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(my_map)
 
# Save map
    my_map.save("./templates/map.html")