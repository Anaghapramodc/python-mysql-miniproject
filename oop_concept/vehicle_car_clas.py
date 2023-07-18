class vehicle:
    def __init__(self, make, model, year, colour, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = mileage

    def drive(self, distance):
        self.distance = distance
        print(f"the distance covered is {self.distance}km")

    def get_info(self):
        print(
            f"the vehicle make is {self.make}, model is {self.model} ,year is {self.year} ,colour is {self.colour} and mileage is {self.mileage} ")


class car(vehicle):

    def __init__(self, make, model, year, colour, mileage, num_door, engine_type):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = mileage
        self.num_door = num_door
        self.engine_type = engine_type

    def get_info(self):
        print(
            f"the vehicle make is {self.make}, model is {self.model} ,year is {self.year} ,colour is {self.colour} ,mileage is {self.mileage} ,num_door is {self.num_door} and engine_type is {self.engine_type}")


vehicle = vehicle("as12", "bd2002", 2022, "white", 54.69)
vehicle.drive(100)
vehicle.get_info()
car = car("f2", "i20", 2023, "red", 60.02, 5, "carbon cumbustion")
car.get_info()
