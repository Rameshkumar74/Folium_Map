import folium

# mapobj = folium.Map(location=[12.97428208664007, 77.61754989624025], zoom_start=12)

# folium.Circle(radius=4000,location=[12.974319881407284, 77.50726156338007]).add_to(mapobj)

# mapobj.save('output.html')

mapobj1 = folium.Map(location=[12.822049576003264, 77.68956593796133], zoom_start=12)

folium.Circle(radius=4000,location=[12.822049576003264, 77.68956593796133]).add_to(mapobj1)

folium.Marker([12.836068512875475, 77.68006213031447], popup = "BOMMA HOSPITAL").add_to(mapobj1)

mapobj1.save('output.html')
