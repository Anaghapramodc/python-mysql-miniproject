"""
a function is a block of code.
it executed whenever the function is called.
1)user defined
2)bultin
3)lambda
"""
# #1)user defined funtion
# def test_function():#the funtion is defined by user
#     print("hai world")
# test_function()#function call
#
# def sum():
#     a=int(input("enter the variable"))#local variables
#     b=int(input("enter the variable"))
#     c=a+b
#     print(c)
# sum()
#
# a=int(input("enter the variable"))#global variables
# b=int(input("enter the variable"))
# def sum():
#     c=a+b
#     print(c)
# sum()
#
# def sum(a,b):#parametrs
#     c=a+b
#     print(c)
# sum(12,32)#arguments
#
# def sum(a,b):
#     c=a+b
#     return c
# print(sum(12,2))
#
# def sum(a,b,e,d):
#     c=a+b
#     x=e+d
#     return c,x
# print(sum(12,2,3,4))
#
# def sum(a,b,e,d):
#     c=a+b
#     x=str(input("enter the string"))
#     return c,x
# print(sum(12,2,3,4))
#
#
# #arguments
# #1)possitional arguments
# def sum(a,b):
#     c=a+b
#     return c
# print(sum(12,2))
#
# #2)arbitary arguments
# def name(*persn):
#     print("name=",persn)
# name("anagha","akshaya","ponnu")
#
# def name(*persn):
#     print("name=",persn)
# name("anagha")
#
# def name(*persn):
#     print("name=",persn)
# name("anagha","akshaya")
#
# #3)keyword argument
# def name(a,b,c):
#     print("name=",b)
# name(c="anagha",a="akshaya",b="ponnu")
#
# def name(a,b,c):
#     print("name=",b)
# name(b="anagha",a="akshaya",c="ponnu")
#
# def name(a,b,c):
#     print("name=",c)
# name("anagha",c="akshaya",b="ponnu")
#
# def name(a,b,c,d):
#     print("name=",c)
# name("anagha",c="akshaya",d="ponnu",b="ammu")
#
# def name(a,b,c,d,e):
#     print("name=",c)
# name("anagha",c="akshaya",e="ponnu",b="ammu",d="pramod")
#
# def name(a,b,c,d,e,f):
#     print("name=",c)
# name("anagha",c="akshaya",d="ponnu",b="ammu",e="pramod",f="sreeja")

#4)arbitary keyword arguments
def name(**names):
    print("name=",names['b'])
name(c="anagha",a="akshaya",b="ponnu")

def name(**names):
    print("name=",names['b'])
name(b="anagha",a="akshaya",c="ponnu")

#default value
def contry(name="india"):
    print("i am from "+name)
contry()
contry("newyork")
contry("sweden")

def food_items(food):
    for i in food:
        print(i)
name=["biriyani","veg","rice"]
food_items(name)




















