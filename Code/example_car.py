class car:
    def __init__(self,colour):
        self.colour = colour

my_car = car('blue')

def crash(car1,car2):
    car1.colour = 'burnt'

crash(car('red'), my_car)
