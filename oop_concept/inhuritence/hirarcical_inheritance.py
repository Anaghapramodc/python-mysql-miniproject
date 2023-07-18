"""
multiple child class accepts one parant class
"""
class vehicle:
    def vehicle_info(self):
        print("this is vehicle")

class car(vehicle):
    def car_info(self,name):
        print("car name is",name)

class truck(vehicle):
    def truck_info(self,name):
        print("truck name is",name)
obj1=car()
obj1.car_info("BMW")
obj1.vehicle_info()
obj2=truck()
obj2.truck_info("ford")
obj2.vehicle_info()

