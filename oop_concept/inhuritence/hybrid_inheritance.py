"""
combination of different inheritance is called hybrid inheritance
"""


class vehicle:
    def vehicle_info(self):
        print("this is vehicle")



class car(vehicle):
    def car_info(self, name):
        print("car name is", name)


class truck(vehicle):
    def truck_info(self, name):
        print("truck name is", name)


class sportcar(car, vehicle):
    def sportcar_info(self):
        print("inside the sport car class")


s_car = sportcar()
s_car.car_info("bmw")
s_car.vehicle_info()
obj1 = car()
obj1.car_info("BMW")
obj1.vehicle_info()
obj2 = truck()
obj2.truck_info("ford")
obj2.vehicle_info()
