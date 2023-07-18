l=[]
r=int(input("enter the range of the list"))
print("enter the numbers")
for i in range(r):
    x=int(input())
    l.insert(0,x)
print(l)
sum=0
for i in l:
    sum=sum+i
print("sum of numbers=",sum)