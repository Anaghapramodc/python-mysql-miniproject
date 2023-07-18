"""
to initialise objects
paramised constructer
defult value constructer

"""

"""
different types of constructers 
default
parametersided constructers
parameterised value contructers
"""

class car:
    def __init__(self,name,model):#constructer:-to initialise object
        self.name=name
        self.model=model

    def test(self):#methord creat in function
        print("hai dear")
    def __str__(self):#print string model:-to print object
        return f"{self.name} is {self.model} model car"

car1=car('BMW',2018)
print(car1)
car1.model=2023
del car1.model#to delete objects
car1.test()
car2=car('vento',2015)
print(f"{car1.name} is {car1.model} model car")
print(f"{car2.name} is {car2.model} model car")
