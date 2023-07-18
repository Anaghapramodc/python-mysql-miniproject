#creat calculator
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
print(x,"+",y,"=",x+y)
print(x,"-",y,"=",x-y)
print(x,"*",y,"=",x*y)
print(x,"/",y,"=",x/y)
print(x,"%",y,"=",x%y)
print(x,"**",y,"=",x**y)
print(x,"//",y,"=",x//y)
print(x,">",y,"=",x>y)
print(x,"<",y,"=",x<y)
print(x,"==",y,"=",x==y)
print(x,"!=",y,"=",x!=y)
print("(",x,">",y,")","AND","(",x,"<",y,")","=",x>y and x<y)
print("(",x,">",y,")","OR","(",x,"<",y,")","=",x>y or x<y)
print("(",x,">",y,")","NAND","(",x,"<",y,")","=",not(x>y and x<y))
print("(",x,">",y,")","NOR","(",x,"<",y,")","=",not(x>y or x<y))
print("\n")


print("1-addition")
print("2-subtraction")
print("3-multiplication ")
print("4-division")
print("5-modules")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
choise=int(input("Enter your choise"))
if(choise==1):
      print("addition=",a+b)
elif(choise==2):
     print("subtraction=",a-b)
elif(choise ==3):
    print("multiplication=", a*b)
elif (choise ==4):
        print("division=", a/b)
elif (choise == 5):
        print("modules=", a%b)



