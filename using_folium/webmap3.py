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
def color_fill(x):
    if x<= 1000:
        y = "blue"
    elif x>1000 and x <=2000:
        y = "green"
    elif x>2000 and x<=4000:
        y = "orange"
    else:
        y = "black"
    return y

map = folium.Map((37.6999016, -118.8710022),  tiles="Mapbox Bright")
fg1 = folium.FeatureGroup(name = "My Fg1")
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
    fg1.add_child(folium.CircleMarker(location=x, popup=folium.Popup(iframe), radius= 6.0 , tooltip= "beware", fill_color = color_fill(volcanoes_desp[x][4]), color = "grey", opacity = 0.6))


fg2 = folium.FeatureGroup(name = "My Fg2")
fg2.add_child(folium.GeoJson(data= open("world.json", "r", encoding="utf-8 sig" ).read(),
                            style_function= (lambda x : {"fillColor":'green' if x["properties"]["POP2005"] < 10000000 else 'yellow' if (x["properties"]["POP2005"]<=10000000 and x["properties"]["POP2005"]<=100000000) else 'red'})))


map.add_child(fg2)
map.add_child(fg1)

map.add_child(folium.LayerControl())
map.save("map3.html")