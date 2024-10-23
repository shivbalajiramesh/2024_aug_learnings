#https://www.youtube.com/watch?v=97V7ICVeTJc

from abc import ABC, abstractmethod

class vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(vehicle):

    def go(self):
        print('You drive the car')
    def stop(self):
        print('You stop the car')

class motorcycle(vehicle):

    def go(self):
        print('You ride the motorcycle')
    def stop(self):
        print('You stop the motorcycle')

class boat(vehicle):

    def go(self):
        print('You sail the boat')
    def stop(self):
        print('You anchor the boat')



car_one = car()
motorcycle_one = motorcycle()
boat_one = boat()

print('\n')
car_one.go()
car_one.stop()
motorcycle_one.go()
motorcycle_one.stop()
boat_one.go()
boat_one.stop()

