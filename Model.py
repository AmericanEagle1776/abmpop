import numpy as np
import matplotlib as plt
import Human
import Mosquito

class Model:

    def __init__(self, nh, nm ):

        self.humans = []
        self.mosquitoes = []

        self.n_human = nh
        self.n_mosquito = nm

        for humans in range(n_human):

            self.humans.append(Human())

        for mosquitos in range(n_mosquito):

            self.mosquitoes.append(Mosquito())


    def update(self):

        for human in self.humans:
            human.move()

        for mosquito in self.mosquitoes:

            mosquito.move()
            for victim in self.humans:
                if abs(victim.coordinate - mosquito.coordinate) <= (3, 3):

                    mosquito.bite()
