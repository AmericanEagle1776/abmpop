import numpy as np
import matplotlib as plt
import Human
import Mosquito

class Model:

    def __init__(self, nh, nm ): #initialise the starting situation

        self.humans = [] #our humans
        self.mosquitoes = [] #our mosquitoes

        self.n_human = nh
        self.n_mosquito = nm

        for humans in range(n_human):

            self.humans.append(Human())

        for mosquitos in range(n_mosquito):

            self.mosquitoes.append(Mosquito())


    def update(self): #new timestep

        for human in self.humans: #human activity
            human.move()

        for mosquito in self.mosquitoes: #mosquito activity

            mosquito.move()

            for victim in self.humans: # bite if in vicinity # TODO: only bite once per timestep
                if abs(victim.coordinate - mosquito.coordinate) <= (3, 3):

                    mosquito.bite()


            chance = np.random.randint(0, 10) # for a random occurence
            if (mosquito.blood_meals=2 & chance >= 5): #breeds half the timne it already has fed twice
                mosquito.breed()
            elif(mosquito.blood_meals = 3): # always bites if it has fed 3 times
                mosquito.breed()
            else:
                continue