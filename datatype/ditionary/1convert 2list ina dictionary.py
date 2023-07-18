#convert 2 list into a dictionary
list1=["name","age","course","batch"]
list2=["anagha",22,"python","3rd"]
d1={}
i=0
while i<4:
    x=list1[i]
    y=list2[i]
    d={x:y}
    d1.update(d)
    # print(d1)
    i+=1

print(d1)

list1=["name","age","course","batch"]
list2=["anagha",22,"python","3rd"]
dict1=dict(zip(list1,list2))
print(dict1)

