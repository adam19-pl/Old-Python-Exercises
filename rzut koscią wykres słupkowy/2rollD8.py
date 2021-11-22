from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(8000):
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)


frequency = []
max_result = die_1.side_numbers + die_2.side_numbers

for value in range(2, max_result + 1):
    freq = results.count(value)
    frequency.append(freq)


x_values = list(range(2, max_result + 1))

data = [Bar(x = x_values, y = frequency)]

x_axis_config = {'title': 'Suma liczby oczek z dwóch kości typu D8 ','dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wyniki rzucania dwóch kości typu D8  pięć tyśiecy razy : ',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D8-razydwa.html')