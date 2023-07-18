# Write a python program to find largest number in a given list with out using max()
l=[]
r=int(input("enter the range of the list"))
print("enter the numbers")
for i in range(r):
    x=int(input())
    l.append(x)
print(l)
l.sort()
print("largest number=",l[-1])

# l=[12,4,5,7,8,6,4,2,1,5]
# print("largest number=",max(l))