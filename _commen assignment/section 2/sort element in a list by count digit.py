# l=["ab","a","Acsd","asd"]
# l.sort(reverse=False,key=len)
# print(l)
l=["ab","a","acsd","asd"]
x=0
c=0
d={}
for i in l:
    for j in i:
        c=c+1
    d[c]=i
    c=0
print(d)
l2=[]
x=list(d.keys())
for i in range(len(x)):
    for j in x:
       l2.append(min(x))
       x.remove(min(x))
l3=[]
for i in range(len(l2)):
    z=l2[i]
    l3.append(d[z])
print(l3)
