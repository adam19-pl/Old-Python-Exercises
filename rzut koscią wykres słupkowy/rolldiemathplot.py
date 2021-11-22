from die import Die
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()

results = [die_1.roll_die() + die_2.roll_die() for roll_num in range(10000)]
max_result = die_1.side_numbers + die_2.side_numbers
frequency = [results.count(value) for value in range(2, max_result + 1)]


plt.style.use('seaborn-whitegrid')

    # zdefiniowanie zmiennych oraz wywołanie metody tworzącej wykres (subplots)
fig, ax = plt.subplots()

ax.scatter(max_result, frequency, c ='green', s=100)
    # Nadanie tytułu wykresu oraz jego wielkośći
ax.set_title("Symulacja 1000 razy rzutu 2 koścmi typu D6", fontsize=10)
    # nadanie tytułu osi x
ax.set_xlabel("suma oczek", fontsize=10)
    # nadanie tytułu osi y
ax.set_ylabel("Ilość wystąpień ", fontsize=10)

    # wywołanie funkcji która tworzy wykresdd
plt.show()
