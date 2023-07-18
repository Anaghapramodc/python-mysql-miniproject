#the circle class models a circle with a radiourand colour
#attributeas : radious,colour
#methods:
# circle Pir2
# getradius() r
# getcircumference() 2pir
# area() pir2
class circle:
    def __init__(self,radious,colour):
        self.radious=radious
        self.colour=colour

    def circle(self):
        print("Equation of the circle=pi*r^2")

    def getradius(self):
        print("radious of the circle=",self.radious)

    def getcircumference(self):
        print("circumference of circle=",2*3.14*self.radious)

    def getarea(self):
        print("area of the circle=",3.14*self.radious*self.radious)

c=circle(5,"red")
c.circle()
c.getradius()
c.getcircumference()
c.getarea()
c.radious