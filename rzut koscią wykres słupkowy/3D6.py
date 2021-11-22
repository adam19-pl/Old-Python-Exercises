from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll_die() + die_2.roll_die() + die_3.roll_die() for roll_num in range(1000)]
#przykład listy złożonej -- można stosować zamiast pętli for
#results = []
#
#for roll_num in range(8000):
#   result = die_1.roll_die() + die_2.roll_die() +die_3.roll_die()
#   results.append(result)


max_result = die_1.side_numbers + die_2.side_numbers + die_3.side_numbers
frequency = [results.count(value) for value in range(3, max_result + 1)]

x_values = list(range(3, max_result + 1))

data = [Bar(x = x_values, y = frequency)]

x_axis_config = {'title': 'Suma oczek trzech kości', 'dtick': 1}
y_axis_config = {'title': 'Cześtotliwość wyśtąpień podczaś rzucania 1000 razy'}

my_layout = Layout(title='Symulacja rzucania 3 kośćmi typu D6 1000 razy', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='3d6-symulacja.html')
