import folium

latitude_list = [30.333, 30.300, 30.321]
longtitude_list = [77.333, 77.000, 77.321]

map1 = folium.Map(location=[60.170667, 24.941497])

map1.save("./templates/map.html")