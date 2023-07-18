class vehicle:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

    def show(self):
        print("details: \n name=",self.name,"\n colour=",self.colour)

car=vehicle('bmw','red')
car.show()

jeep=vehicle('ford','black')
jeep.show()