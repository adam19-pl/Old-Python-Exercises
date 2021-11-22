import matplotlib.pyplot as plt
import numpy as np
# importowanie biblioteki numpy w celu zainicjowania metody arange - pozwoli ona na dostarzenie argumentów o typie float

while True:
    try:
        first_number = float(input("Wprowadź liczbę od której chcesz liczyć potęgę : "))
        second_number = float(input("Wprowadź liczbę do której chcesz liczyć potęge : "))
        power_number = float(input("Wprowadź liczbę, która będzie odpowiadała za potęgę : "))
    except ValueError:
        print("Wprowadziłeś błędne dane .... ")

    else:

        if first_number == second_number:

            # wykorzystanie metody arange , aby dostarczyć argumenty w typie float
            numbers = np.arange(first_number, second_number + 1)
            cubes = [x ** power_number for x in numbers]

            plt.style.use('seaborn-whitegrid')

            fig, ax = plt.subplots()
            ax.scatter(numbers, cubes, c='red', s=30)
            ax.set_title(f'Liczby do potęgi {power_number}', fontsize=15)
            ax.set_xlabel('Liczby  ', fontsize=10)
            ax.set_ylabel('Potęga', fontsize=10)

        elif first_number > second_number:
            numbers = np.arange(second_number, first_number + 1)
            cubes = [x ** power_number for x in numbers]
            plt.style.use('seaborn-whitegrid')

            fig, ax = plt.subplots()

            ax.plot(numbers, cubes, linewidth= 1)
            ax.scatter(numbers, cubes, c = cubes, cmap = plt.cm.Blues, s = 30)
            ax.set_title(f'Liczby do potęgi {power_number}', fontsize = 15)
            ax.set_xlabel('Liczby  ', fontsize = 10)
            ax.set_ylabel('Potęga', fontsize = 10)

        else:
            numbers = np.arange(first_number, second_number + 1)
            cubes = [x ** power_number for x in numbers]

            plt.style.use('seaborn-whitegrid')

            fig, ax = plt.subplots()

            ax.plot(numbers, cubes, linewidth= 1)
            ax.scatter(numbers, cubes, c = cubes, cmap = plt.cm.Blues, s = 30)
            ax.set_title(f'Liczby do potęgi {power_number} ', fontsize = 15)
            ax.set_xlabel('Liczby  ', fontsize = 10)
            ax.set_ylabel('Potęga', fontsize = 10)

        # zapisywanie do pliku wykresu
        want_save = input("Czy chcesz zapisać wykres ? [y/n] :")
        if want_save == 'y':
            file_name = input("Podaj nazwę, jak chcesz zapisać plik : ")
            plt.savefig(f'{file_name}.png', bbox_inches='tight')
            plt.show()
        else:
            plt.show()

        keep_runing = input("Czy chcesz zakończyć program ?  [y/n] : ")
        if keep_runing == 'y':
            break