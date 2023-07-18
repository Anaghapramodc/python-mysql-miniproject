"""
same methords are used in the parant class and child class
"""

class A:
    def name(self):
        print("name start with letter A")

    def eg(self):
        print("Anagha")

class B(A):
    def name(self):
        print("name start with letter B")

    def eg(self):
        print("Bindhu")

b=B()
b.name()
b.eg()

a=A()
a.name()
a.eg()

"""
methord overloading

comple time polimorfism
same methord with differentr parameter 
python does not support
"""