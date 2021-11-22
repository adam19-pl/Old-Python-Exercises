from die import Die
import matplotlib.pyplot as plt
import pygal

die_1 = Die()
die_2 = Die()


results = [die_1.roll_die() + die_2.roll_die() for x in range(1000)]

max_result = die_1.side_numbers + die_2.side_numbers
frequency = [results.count(value) for value in range(2,max_result + 1)]


hist=pygal.Bar()
hist.title=" Wynik rzucania dwóch kości typu D6 1000 razy"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Liczba oczek"
hist.y_title="Częstotliwość wyrzucenia takiej liczby"
hist.add('D6',frequency)
hist.render_to_file('wizualizacja.html')