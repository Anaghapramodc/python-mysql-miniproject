# Write a python program to find the common numbers from two lists
list1=[1,5,4,2,7]
list2=[1,2,4,5,1,7]
l=[]
for i in list1:
    for j in list2:
        if i==j:
           l.append(i)
           break
print("commen numbers in the list",l)