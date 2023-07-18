#rename key of a dictionary
dict1={"red":1,"blue":2,"green":3,"yellow":4}
dict2={}
for i in dict1:
    x=input("enter the  key name")
    v=dict1.get(i)
    dict2.setdefault(x,v)
print(dict2)
