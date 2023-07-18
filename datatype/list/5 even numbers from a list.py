# Write a python program to print all even numbers from a given list
list=[1,2,4,5,7,8,4,9,6,1,22,12]
l=[]
for i in list:
    if i%2==0:
        l.append(i)
print("even numbers=",l)