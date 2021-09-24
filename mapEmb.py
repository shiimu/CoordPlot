import folium

def centerLocation():
    from dbGet import longt, latt

    map1 = folium.Map(location=[latt, longt])
    map1.save("./templates/map.html")
    return latt, longt