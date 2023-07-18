"""
armstrong number=1634--->1^4+6^4+3^4+4^4=1634
                =370----->3^3+7^3+0^3=370
"""
n=int(input("enter the number"))
n1=n
c=len(str(n))
sum=0
i=1
while i<=c:
       r1=n1%10
       t=r1**c
       n1=n1//10
       sum=sum+t
       i+=1
if sum==n:
    print(n," is armstrong number")
else:
    print(n," is not armstrong number")