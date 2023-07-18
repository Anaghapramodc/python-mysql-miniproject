r=int(input("enter the range "))
sum=0
for i in range(1,r+1):
    x=str(i)
    l=len(x)
    for j in x:
        y=int(j)
        sum=sum+y**l
    if sum==i:
        print(i)
    sum=0
