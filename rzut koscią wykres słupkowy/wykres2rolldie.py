# Zaimportowanie bibliotek potrzebnych do utworzenia histogramu - wykresu słupkowego
from plotly.graph_objs import Bar, Layout
from plotly import offline
# Zaimportowanie klasy z pliku die.py
from die import Die

# Utworzenie dwóch obiektów na podstawie klasy Die
die_1 = Die()
die_2 = Die()

# Lista która będzie przechowywać wyniki rzutu dwóch kości
results = []

# Pętla odpowiadająca za dodawanie wyników rzutów dwóch kości 1000 razy do listy results
for roll_number in range(1000):
    # Wykorzystanie metody klasy Die odpowiadającej za wybór liczby o 1 do liczby scianek
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)

# Lista przechowująca liczbę najczęściej występujących elementów na liscie results
frequencies = []

# Zdefiniowanie maxymalnego elementu jaki może wystąpić (czyli 12 - liczba scianek jednej kości to 6 )
max_results = die_1.side_numbers + die_2.side_numbers

# Pętla mająca za zadanie dodać do listy ilość elementów powtarzających się w liscie results
for value in range(2, max_results + 1):  # Pętla Sprawdza zakres elemetów od 2 do max_results+1 dla value
    # do zmiennej frequency-  przypisujemy ilość powtarzających się elementów w liscie results
    frequency = results.count(value)
    frequencies.append(frequency)  # dodajemy zmienną frequency do listy frequencies

# zmienna która będzie przechowywać wartości osi x -- potrzebne do opisu wykresu
x_values = list(range(2, max_results + 1))

# Zmienna która przechowuję wartości potrzebne do przekazania danych dla wykresu słupkowego
data = [Bar(x=x_values, y=frequencies)]

# Zmienna przechowująca informację dotyczące jej opisu w słowniku -- reprezentuje os X
x_axis_config = {'title': 'Wynik', 'dtick': 1}

# Zmienna przechowująca informację dotyczące jej opisu w słowniku -- reprezentuje os y
y_axis_config = {'title': 'Częstotliwość występowania wartości'}

# Zmienna przechowująca  i implementująca informację dotyczące tytułu wykresu, osi x , osi y
my_layout = Layout(title='Wyniki najczęściej wypadanych oczek rzutu dwoma kośmi 1000 razy',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
# Rysowanie histogramu poprzez dostarczenie odpowiednich wartośći oraz podanie nazwy pliku
offline.plot({'data': data, 'layout': my_layout}, filename='2D6.html')
