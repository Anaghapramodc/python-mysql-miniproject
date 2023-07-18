n1=int(input("enter the number"))
n2=int(input("enter the number"))
list1=[]
list2=[]
list3=[]
for i in range(1,n1):
    if n1%i==0:
        x=list1.append(i)
for j in range(1,n2):
    if n2%j==0:
        y=list2.append(j)
print(list1)
print(list2)
for l in list1:
    for t in list2:
        if l==t:
            list3.append(l)
print(f"greatest common devided={max(list3)}")



# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# gcd=1
# for i in range(1,min(n1,n2)):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print(f"greatest common devided={gcd}")











