import folium
from folium import plugins
import csv

mammoth_map = folium.Map(location=[40, -100], zoom_start=3, tiles='Stamen Terrain')

with open('mammoth_finds.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__()
    mammoth_lat_lng = [ [ line[3], line[4], ] for line in reader ]

mammoth_map.add_child(plugins.HeatMap(mammoth_lat_lng))

filename = 'mammoth_heatmap.html'
mammoth_map.save(filename)
print('Heatmap saved to ' + filename)
