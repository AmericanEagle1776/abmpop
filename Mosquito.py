import numpy as np

class Mosquito:

    def __init__(self, blood_meals = 0):

        x_coordinate = np.random.randint(0, 100)
        y_coordinate = np.random.randint(0, 100)

        self.coordinate = (x_coordinate, y_coordinate)

        self.blood_meals = blood_meals

    def bite(self):

        self.blood_meals +=1



    def breed(self):




