import numpy
import pandas
import folium


def set_colour(height):
    if height <= 1000:
        return "green"
    elif height <= 3000:
        return "orange"
    else:
        return "red"


world_map = folium.Map(location=[0, 0], zoom_start=4, tiles="OpenStreetMap")
volcanoes = pandas.read_csv("Volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])
name = list(volcanoes["NAME"])
volcanoes_layer = folium.FeatureGroup(name="volcanoes_layer")

html = """<h4>%s</h4> Height: %d meters"""

for lt, ln, el, nm in zip(lat, lon, elev, name):
    i_frame = folium.IFrame(html=html % (nm, el), width=200, height=100)
    volcanoes_layer.add_child(folium.Marker(location=[lt, ln],
                                            popup=folium.Popup(i_frame),
                                            icon=folium.Icon(
                                                color=set_colour(el))))
world_map.add_child(volcanoes_layer)
world_map.save("Map1.html")

