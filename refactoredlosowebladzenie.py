import matplotlib.pyplot as plt
from random import choice


class RandomWalk():

    def __init__(self,num_points = 50000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]


    def get_step(self):

        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        move = direction * distance
        return move



    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_move = self.get_step()
            y_move = self.get_step()

            if x_move == 0 and y_move == 0:
                continue


            x = self.x_values[-1] + x_move
            y = self.y_values[-1] + y_move

            self.x_values.append(x)
            self.y_values.append(y)

while True:
    rw = RandomWalk()

    rw.fill_walk()
    point_numbers = range(rw.num_points)

    plt.style.use('seaborn-whitegrid')

    fig,ax = plt.subplots(figsize = (15,9))

    ax.scatter(0,0, c= "red", s = 200)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c= "yellow", s = 200)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues,edgecolor = 'none', s = 1)

    #Ukrycie lini wykresów x oraz y, aby nie rozpraszały widoku błądzenia losowego
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    want_save = input("Czy chcesz zapisać wykres ? [y/n] :")
    if want_save == 'y':
        file_name = input("Podaj nazwę, jak chcesz zapisać plik : ")
        plt.savefig(f'{file_name}.png', bbox_inches = 'tight')

    plt.show()

    keep_runing = input("Czy chcesz zakończyć działanie programu ? [y/n] :")
    if keep_runing == 'y':
        break