import json

from plotly import offline
from plotly.graph_objs import Layout, Scattergeo

file1 = "earthquake.geojson"
with open(file1, encoding= "utf-8") as f:
    content = json.load(f)

file_readable = "earthquake_readable.json"

with open(file_readable,'w') as f:
    json.dump(content,f,indent=4)


all_dict = content['features']
meta_data_title = content['metadata']['title']
print(len(all_dict))

mags = []
latitudes = []
longitudes = []
places = []

for specify_dict in all_dict:
    mag = specify_dict['properties']['mag']
    place = specify_dict['properties']['title']
    latitude = specify_dict['geometry']['coordinates'][1]
    longitude = specify_dict['geometry']['coordinates'][0]

    mags.append(mag)
    places.append(place)
    latitudes.append(latitude)
    longitudes.append(longitude)

map_data = [{
            'type': 'scattergeo',
            'text' : places,
            'lon': longitudes,
            'lat': latitudes,
            'marker': {
            'size': [5 * mag for mag in mags],
            'color': mags,
            'colorscale' : 'inferno',
            'reversescale' : True,
            'colorbar': {'title' : 'siła trzęsienia'}
            },}]

my_layout = Layout(title = meta_data_title)
fig = {'data':map_data, 'layout' : my_layout}
offline.plot(fig,filename='Trzesieniev2.html')