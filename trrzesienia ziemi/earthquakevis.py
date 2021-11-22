import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_earthquake_data = json.load(f)

readable_file = 'data/eq_data_readable_file_m1.json'
with open(readable_file,'w') as f:
    json.dump(all_earthquake_data,f, indent=4)

all_earthquake_dicts = all_earthquake_data['features']
metadata_title = all_earthquake_data['metadata']['title']
print(len(all_earthquake_dicts))

# mags = [earthquake_dict['properties']['mags'] for earthquake_dict in all_earthquake_dicts]
# tak trzeba napisać w przypadku refaktoryzacji kodu :) mniej lini, ten sam efekt
mags = []
szerokosc_geograficzna = []
dlugosc_geograficzna = []
place_name = []
for earthquake_dict in all_earthquake_dicts:

    mag = earthquake_dict['properties']['mag']
    place = earthquake_dict['properties']['title']
    dlugosc = earthquake_dict['geometry']['coordinates'][0]
    szerokosc = earthquake_dict['geometry']['coordinates'][1]

    mags.append(mag)
    dlugosc_geograficzna.append(dlugosc)
    szerokosc_geograficzna.append(szerokosc)
    place_name.append(place)


print(mags[:10])
print(szerokosc_geograficzna[:10])
print(dlugosc_geograficzna[:10])


map_data = [{
            'type': 'scattergeo',
            'text' : place_name,
            'lon': dlugosc_geograficzna,
            'lat': szerokosc_geograficzna,
            'marker': {
            'size': [5 * mag for mag in mags],
            'color': mags,
            'colorscale' : 'inferno',
            'reversescale' : True,
            'colorbar': {'title' : 'siła trzęsienia'}
            },}]

my_layout = Layout(title = metadata_title)
fig = {'data':map_data, 'layout' : my_layout}
offline.plot(fig,filename='Trzesienie_ziemi.html')
