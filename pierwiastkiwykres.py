import matplotlib.pyplot as plt
import math

x = int(input("podaj liczbe od której chcesz zacząć ptegowanie i pierwiastkowanie"))
y = int(input("podaj liczbe do  której chcesz zacząć ptegowac i pierwiastkowac"))
while 0 < x < y:
    # Wykres który przedstawia pierwiastki dla liczb od 1 do 25
    # lista która przechowuje liczby od 1 do 25 - z tych liczb będzie obliczany pierwiastek
    numbers = range(x, y + 1)
    # lista która oblicza pierwiastek z elementów listy numbers, w liście jest również pętla
    squerties = [math.sqrt(x) for x in numbers]
    potega = [x ** 2 for x in numbers]

    # zdefiniowanie stylu wykresu
    plt.style.use('seaborn-whitegrid')

    # zdefiniowanie zmiennych oraz wywołanie metody tworzącej wykres (subplots)
    fig, ax = plt.subplots()

    # Umieszczenie wykresu, który przedstawia kwadraty liczb na podstawie listy number, szerokość lini ustawiona na 3
    ax.plot(numbers, squerties, linewidth=3)
    ax.plot(numbers, potega, linewidth=1)
    # Umieszczenie punktów na rysunku, grubośc punktu zdefiniowana na 100
    ax.scatter(numbers, squerties, c ='green', s=100)
    ax.scatter(numbers, potega, c = 'green', s=50)
    # Nadanie tytułu wykresu oraz jego wielkośći
    ax.set_title("Pierwiastki", fontsize=10)
    # nadanie tytułu osi x
    ax.set_xlabel("liczby", fontsize=10)
    # nadanie tytułu osi y
    ax.set_ylabel("Kwadraty", fontsize=10)

    # wywołanie funkcji która tworzy wykresdd
    plt.show()
    exit()
else:
    print("wprowadziłeś złe dane ... ")
    exit()
