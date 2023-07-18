"""
one child class inheritance 2 parent class
"""
class vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

class car:
    def car_info(self):
        print("inside car class")

class sportscar(car,vehicle):
    def sports_car_info(self):
        print("inside sports car info")

car=sportscar()
car.car_info()
car.vehicle_info()
