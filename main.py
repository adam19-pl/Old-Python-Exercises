#zaimportowanie biblioteki oraz nadanie jej aliasu jako plt
import matplotlib.pyplot as plt



# utworzenie listy, której wartości zostaną zamienione z  wartościami osi x
input_values = [1,2,3,4,5,6]
#utowrzenie 2 list które będą przechowywać wartośći
squares = [1,4,9,16,25,36]
numbers2 = [5,10,15,20,25,30]

#Inicjalizacja stylu wykresu // w powłoce pythona możesz wypisać motywy wpisując po zaimportowaniu biblioteki
# plt.style.available
plt.style.use('Solarize_Light2')
#Fig - zmienna przedstawia caly rysunek, czyli kolekcję wygenerowanych wykresów
#zmienna ax - zawiera jeden wykres na rysunku
#funkcja subplots pozwala na wygenerowanie jednego lub więcej wykresów na jedynm rysunku
fig, ax = plt.subplots()
#funkcja plot odpowiada za wyświetlanie liczb (danych) w logiczny sposób, linewidth określa grubość lini
ax.plot(input_values,squares, linewidth = 3)
ax.plot(input_values, numbers2, linewidth = 3)

# metoda scatter pozwala na rysowanie punktów na wykresie // pierwszym argumentem jest lista wartości umieszczonej na
# osi x , drugim argumentem jest lista przechowująca wartości kwadratów (squares) lub( liczb podwyzszonych o 5(numbers2)
# s odpowiada za wielkość punktu
ax.scatter(input_values, squares, s =100)
ax.scatter(input_values,numbers2, s = 200)


#funkcja set_title pozwala na ustalenie tytułu wykresu, fontsize oznacza rozmiar czczionki
ax.set_title("Kwadraty liczb oraz liczby co 5", fontsize= 18)
#funkcja set_x/ylabel pozwala na nadanie tytułu osi x lub y
ax.set_ylabel("Wartość", fontsize = 14)
ax.set_xlabel("Liczby", fontsize = 14)


#funkcja tick_params określa wielkość parametrów (axis='both') -> X/Y oraz (labelsize) wielkość lini
ax.tick_params(axis = 'both', which='major', labelsize = 10)
#funkcja show odpowiada za wyświetlanie
plt.show()