#operators
#1-->arithmetic operators
x=10
y=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
print(x//y)
#----------------------------------------------------------------------------------------------
#2-->assignment operators
x=10
y=3
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=y
print(x)
x**=y
print(x)
x//=y
print(x)
z=1
t=3
z//=t
print(z)
z=1.0
t=3
z//=t
print(z)
z=1
t=3.0
z//=t
print(z)
#-----------------------------------------------------------------------------------------------------
#3-->comparison operators
x=10
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
#------------------------------------------------------------------------------------------------------
#4-->logic operators
x=10
y=3
print(x>y and x<y)#true and false = false
print(x>y and y<x)#true and true = true
print(x<y and y>x)#false and false = false
print(x>y or x<y)#true or false = true
print(x>y or y<x)#true or true = true
print(x<y or y>x)#false or false = false
print(not(x>y and x<y))#not(true and false) = true
print(not(x>y and y<x))#not(true and true) = false
print(not(x<y and y>x))#not(false and false) = true
print(not(x>y or x<y))#not(true or false) = false
print(not(x>y or y<x))#not(true or true) = false
print(not(x<y or y>x))#not(false or false) = true
#-------------------------------------------------------------------------------------------------------
#5-->identity operators
x=["apple","orange"]
y=["apple","orange"]
print(x is y)# false-->memmory location of x and y are different
z=x#assigning the value of x into z also the memmory location of x and z may same
print(z is x)# true-->memory location of z and x are same
print(x is z)# true-->memory location of z and x are same
print(x==y)
x=["apple","orange"]
y=["apple","mango"]
print(x is y)# false-->memmory location of x and y are different
z=x#assigning the value of x into z also the memmory location of x and z may same
print(z is x)# true-->memory location of z and x are same
print(x is z)# true-->memory location of z and x are same
print(x==y)
x=[3,2]
y=[3,2]
print(x is y)# false-->memmory location of x and y are different
z=x#assigning the value of x into z also the memmory location of x and z may same
print(z is x)# true-->memory location of z and x are same
print(x is z)# true-->memory location of z and x are same
print(x==y)
x=["apple","orange"]
y=["apple","orange"]
print(x is not y)# true-->memmory location of x and y are different
z=x#assigning the value of x into z also the memmory location of x and z may same
print(z is not x)# flase-->memory location of z and x are same
print(x is not z)# false-->memory location of z and x are same
print(x!=y)
x=["apple","orange"]
y=["apple","mango"]
print(x is not y)# true-->memmory location of x and y are different
z=x#assigning the value of x into z also the memmory location of x and z may same
print(z is not x)# flase-->memory location of z and x are same
print(x is not z)# false-->memory location of z and x are same
print(x!=y)
x=[3,2]
y=[3,2]
print(x is not y)# false-->memmory location of x and y are different
z=x#assigning the value of x into z also the memmory location of x and z may same
print(z is not x)# true-->memory location of z and x are same
print(x is not z)# true-->memory location of z and x are same
print(x!=y)
#___________________________________________________________________________________________
#6-->Membership operators
x=["apple","orange"]
print("mango" in x)
print("apple" in x)
print("mango" not in x)
print("apple" not in x)


