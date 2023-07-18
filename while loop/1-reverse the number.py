#reverse of a number

n=int(input("enter the number"))
t=n
sum=0
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
print("reverse number of",t,"is",sum)
#
#
#
#
# n=int(input("enter the number"))
# n1=n2=n
# c=0
# sum=0
# while n>0:
#     r=n%10
#     n=n//10
#     c=c+1
# i=c-1
# while i!=-1:
#        t=10**i
#        r1=n1%10
#        p=r1*t
#        n1=n1//10
#        sum=sum+p
#        i-=1
# print("reverse number of",n2,"is",sum)

# n=int(input("enter the number"))
# t=n
# c=0
# while n>0:
#     r=n%10
#     n=n//10
#     c=c+1
#
# print("COUTN OF DIGITS OF",t,"=",c)















