from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()

results = []

for roll_numbers in range(1000):
    result = die_1.roll_die()
    results.append(result)

frequencies = []

for value in range(1, die_1.side_numbers + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, die_1.side_numbers + 1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wyniki najczęściej wypadanych oczek rzutu kością 1000 razy',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D6.html')
