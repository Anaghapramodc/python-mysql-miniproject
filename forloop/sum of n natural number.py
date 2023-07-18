#find sum of n natural number

n=float(input("enter the range of the number"))
if n>0:
    sum=n*(n+1)/2
    print("sum of",n,"natural number",sum)
else:
    print("no value")

#using for loop
print("sum of n natural number")
num=int(input("enter the range of the number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)
