n=int(input("enter the number"))
c=0
for i in range(1,n):
    if n%i==0:
        c=c+i
if n==c:
    print(n,"is a perfect number")
else:
     print(n, "is not perfect number")