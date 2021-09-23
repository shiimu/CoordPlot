import folium

latitude_list = [30.333, 30.300, 30.321]
longtitude_list = [77.333, 77.000, 77.321]

def centerLocation():
    from dbGet import longt, latt

    map1 = folium.Map(location=[latt, longt])
    map1.save("./templates/map.html")
    return latt, longt