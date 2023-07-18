#werite a program to print factorial of a number
n=int(input("enter the number"))
r=1
for i in range(1,n+1):
    r=r*i
print(n,"!=",r)