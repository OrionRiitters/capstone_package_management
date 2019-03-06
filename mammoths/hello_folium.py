import folium

map_mn = folium.Map(location=[44.975, -93.275], zoom_start=15)

folium.Marker([44.9729, -93.2831], popup='Minneapolis College').add_to(map_mn)

map_mn.save('hello_map.html')
