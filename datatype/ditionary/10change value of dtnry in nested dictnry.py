#change value of a keys in a nested list
dict1={"animals":{"dog":"black","cat":"brown","caw":"white"}}
dict2={}
for i in dict1:
    for j in dict1.get(i):
        # print(j)
        x=input("enter the new value")
        dict2.setdefault(j,x)
y=dict1.fromkeys(dict1,dict2)
print(y)



