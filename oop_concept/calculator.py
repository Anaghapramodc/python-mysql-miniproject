#mathamatical calculator

class calculator:
    def addition(self):
        print(a+b)

    def subtraction(self):
        print(a-b)

    def multiplication(self):
        print(a*b)

    def devision(self):
        print(a/b)

a=int(input("enter the number:"))
b=int(input("enter the number:"))
obj=calculator()
choise=1
while choise!=0:
    print('1-addision')
    print('2-subtraction')
    print('3-multiplication')
    print('4-devision')
    choise=int(input("enter the choise:"))
    if choise==1:
        obj.addition()
    elif choise==2:
        obj.subtraction()
    elif choise==3:
        obj.multiplication()
    elif choise==4:
        obj.devision()
    else:
        print("invalid sintax")



