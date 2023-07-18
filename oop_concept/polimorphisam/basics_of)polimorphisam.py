"""
polymorphism is the ability of an object to take many forms.

"""
class vehicle:
    def __init__(self,name,colour,price):
        self.name=name
        self.colour=colour
        self.price=price

    def show(self):
        print("details",self.name,self.colour,self.price)

    def max_speed(self):
        print("max speed is 150")

    def change_gear(self):
        print("vehicle change 6 gear")

class car(vehicle):
    def max_speed(self):
        print("car max speed is 240")

    def change_gear(self):
        print("car gear 7 gear")

# car=car('ford','grey',2500)
# car.show()
# car.max_speed()
# car.change_gear()
# vehicle=vehicle('bmw','black',123456)
# vehicle.show()
# vehicle.max_speed()
# vehicle.change_gear()

car1=car('bmw','grey',2500)
car2=car('bens','blue',2500)

for x in(car1,car2):
    x.show()
    x.max_speed()
    x.change_gear()
