#multilevel inheritance
class vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

class car(vehicle):
    def car_info(self):
        print("inside car class")

class sportscar(car):
    def sports_car_info(self):
        print("inside sports car info")

car=sportscar()
car.car_info()
car.vehicle_info()
car.sports_car_info()
