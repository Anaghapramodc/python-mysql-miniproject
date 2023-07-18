#single inheritence
class vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

class car(vehicle):
    def car_info(self):
        print("inside car class")
car=car()
car.car_info()
car.vehicle_info()