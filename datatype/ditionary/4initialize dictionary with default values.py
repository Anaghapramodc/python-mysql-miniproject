#initialize dictionary with default values
print("please enter the valid information")
r=int(input("enter the range of the dictionary:"))
dict1={}
for i in range(r):
    # print(i)
    x=input("enter the key :")
    y=input(f"enter the value of {x} :")
    dict1.setdefault(x,y)
print(dict1)





# print("please enter the valid information")
# n=input("enter your name:")
# a=input("enter your age:")
# c=input("enter your course:")
# b=input("enter your batch number:")
# t=input("enter your class time:" )
# dict1={"name":n,"age":a,"course":c,"batch":b,"time":t}
# print(dict1)