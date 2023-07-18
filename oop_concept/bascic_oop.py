"""
object oriented programming
class-collection of atributes and behaviors.it is a blue print for the object.
object-it is an entity that has atributes and behaviors.
atributes-name,age,colour
behavior-danceing,singing

oop consepts:-
abstraction
encapsulation
inheritence
polymorphism
"""

class Myclass:
    x=5
print(Myclass)

obj=Myclass()
print(obj.x)

class car:
    name=''
    model=int

car1=car()
car1.name='vento'
car1.model=2018
print(f"{car1.name} is {car1.model} model car")

car2=car()
car2.name='BMW'
car2.model=2020
print(f"{car2.name} is {car2.model} model car")