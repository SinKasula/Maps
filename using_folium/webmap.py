import folium
from pandas import read_csv
data = read_csv("Volcanoes.txt")
lat  = list(data["LAT"])
lon = list(data["LON"])
location = list(zip(lat,lon))
name = list(data["NAME"])
v_location = list(data["LOCATION"])
type_v = list(data["TYPE"])
v_status = list(data["STATUS"])
elev_v = list(data["ELEV"])
description = list(zip(name,v_status,v_location,type_v,elev_v))
volcanoes_desp = dict(zip(location,description))
map = folium.Map((37.6999016, -118.8710022),  tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Fg")
html = """<h4>Volcano information:</h4>
Name : %s Volcano<br>
Status : %s<br>
Type : %s <br>
Location : %s <br> 
Height: %s m <br>
 <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">More Information</a>
"""
for x in volcanoes_desp.keys():
    iframe = folium.IFrame(html=html % ( str(volcanoes_desp[x][0]) ,str(volcanoes_desp[x][1]),str(volcanoes_desp[x][3]), str(volcanoes_desp[x][2]), str(volcanoes_desp[x][4]),  str(volcanoes_desp[x][0])), width=300, height=200)
    if volcanoes_desp[x][4] <= 1000 :
        fg.add_child(folium.Marker(location= x, popup= folium.Popup(iframe) ,icon=folium.Icon(color="blue")))
    elif volcanoes_desp[x][4] > 1000 and volcanoes_desp[x][4] <= 2000:
        fg.add_child(folium.Marker(location=x, popup=folium.Popup(iframe), icon=folium.Icon(color="green")))
    elif volcanoes_desp[x][4] > 2000 and volcanoes_desp[x][4] <= 4000:
        fg.add_child(folium.Marker(location=x, popup=folium.Popup(iframe), icon=folium.Icon(color="organge")))
    elif volcanoes_desp[x][4] > 4000 and volcanoes_desp[x][4] <= 6000:
        fg.add_child(folium.Marker(location=x, popup=folium.Popup(iframe), icon=folium.Icon(color="black")))
    else:
        fg.add_child(folium.Marker(location=x, popup=folium.Popup(iframe), icon=folium.Icon(color="pink")))

map.add_child(fg)
map.save("map1.html")