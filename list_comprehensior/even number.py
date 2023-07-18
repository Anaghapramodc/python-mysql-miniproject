list=[1,2,3,4,5,6,7,8,9,10]
l=[]
l1=[]
for i in list:
    if i%2==0:
        l.append(i)
    else:
        l1.append(i)
print("even=",l)
print("odd=",l1)

obj=[(i,'even'if i%2==0 else 'odd') for i in list]
print(obj)
