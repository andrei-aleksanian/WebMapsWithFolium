import numpy
import pandas
import folium

map = folium.Map(location=[0, 0], zoom_start=4, tiles="OpenStreetMap")
volcanoes = pandas.read_csv("Volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
print(volcanoes)
help(folium.IFrame)
help(folium.Popup)

