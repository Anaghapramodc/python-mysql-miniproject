#9+99+999+9999=11106
# r=int(input("enter the range"))
# n=int(input("enter the repeating number"))
# s=""
# sum=0
# for i in range(1,r+1):
#     for j in range(i,2*i):
#        s=s+str(n)
#        c=int(s)
#     sum=sum+c
#     s=""
# print(sum)

s=0
sum=0
r=int(input("enter the range"))
n=int(input("enter the repeating number"))
for i in range(0,r):
    s=s*10+n
    sum=sum+s
print(sum)














