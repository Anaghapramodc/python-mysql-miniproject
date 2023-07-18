r1=int(input("range of main list"))
r2=int(input("range of sub list"))
l1=[]
l2=[]
for i in range(r1):
    x=input("enter the number:")
    l1.append(x)
print(l1)
for j in range(r2):
    y=input("enter the number:")
    l2.append(y)
print(l2)
c=0
for i in l1:
    for j in l2:
        if j==i:
            c=c+1
if c==len(l2):
    print(l2,"is a sublist of",l1)
else:
    print(l2, "is not a sublist of", l1)


