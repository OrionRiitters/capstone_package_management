import folium
import csv

mammoth_colors = {
    'Mammuthus columb': 'green',
    'Mammuthus primigenius': 'blue',
    'Mammuthus hayi': 'purple',
    'Mammuthus exilis': 'red',
    'Mammuthus': 'orange'
}

mammoth_map = folium.Map(location=[40, -120], zoom_start=3, tiles='Stamen Terrain')

mammoth_lat_lng = []

with open('mammoth_finds.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__()

    for line in reader:
        lat = line[3]
        lon = line[4]
        mammoth_lat_lng.append([lat, lon])

        marker_text = f'{line[0]} found in {line[6]}, {line[5]}, {line[7]}.'
        if line[1]:
            marker_text += f' {line[1]}, {line[2]} '

        color = mammoth_colors.get(line[0])

        marker = folium.Marker([lat, lon], popup=marker_text, icon=folium.Icon(color=color))
        marker.add_to(mammoth_map)


map_filename = 'mammoth_marker_map.html'
mammoth_map.save(map_filename)
print('Map saved to ' + map_filename)
