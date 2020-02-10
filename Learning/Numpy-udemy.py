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

avriandlanf = folium.LayerControl()
layerControl = folium.LayerControl(position="topright")

volcanoes_layer = folium.FeatureGroup(name="volcanoes_layer")
population_layer = folium.FeatureGroup(name="population_layer")


html = """<h4>%s</h4> Height: %d meters"""

for lt, ln, el, nm in zip(lat, lon, elev, name):
    i_frame = folium.IFrame(html=html % (nm, el), width=200, height=100)
    # You can add marker clusters as well to make it look much nicer.
    # And make the map smaller on a website!
    volcanoes_layer.add_child(folium.CircleMarker(location=[lt, ln],
                                                  popup=folium.Popup(i_frame),
                                                  radius=6,
                                                  fill_color=set_colour(el),
                                                  color=set_colour(el),
                                                  fill_opacity=1))

population_layer.add_child(folium.GeoJson(data=open("world.json", "r",
                                                    encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"] <
10000000 else "orange" if x["properties"]["POP2005"] < 100000000 else "red"}))


world_map.add_child(population_layer)
world_map.add_child(volcanoes_layer)

world_map.add_child(layerControl)
world_map.save("Map1.html")

