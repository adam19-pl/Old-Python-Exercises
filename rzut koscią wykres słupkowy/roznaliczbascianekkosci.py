from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll_numbers in range(50000):
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)

frequencies = []
max_result = die_1.side_numbers + die_2.side_numbers

for value in range(2, max_result+ 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Suma liczby oczek z dwóch kości','dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wyniki rzucania koścmi typu D6 oraz D10 pięćdziesiąt tyśiecy razy : ',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D6-v2.html')
