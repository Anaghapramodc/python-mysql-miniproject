# write a program to display product of the digits of a number accepted from the user
n=int(input("enter the number"))
p=1
for i in range(0,n+1):
    d=n%10
    p=p*d
    n=n//10
    print("d=",d)
    print("n=",n)
    print("p=",p)
    if  n==0:#d=2 n==0
        break
print("product of the digits =",p)

#
# print(n)
