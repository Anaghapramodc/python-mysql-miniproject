"""
2|12,30
 ------
3|6,15
 ------
  2,5
"""
def lcm(m1,m2):
   if m1!=1 or m2!=1:
       l=[]
       for i in range(2,min(m1,m2)+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                l.append(i)
       # list=[2,3,5,7,11]
       for i in l:
           if m1%i==0 and m2%i==0:
               m1=m1//i
               m2=m2//i
               return i*lcm(m1,m2)
       return m1*m2
m1=int(input("enter the number:"))
m2=int(input("enter the number:"))
print(f"LCM of {m1} and {m2} = {lcm(m1,m2)}")
"""
m1=12 m2=30
common multiplayer-->i=2
m1=12//2=6 m2=30//2=15
return 2*lcm(6,15)

m1=6 m2=15
common multiplayer-->i=3
m1=6//3=2 m2=15//3=5
return 2*3*lcm(2,5)

m1=2 m2=5
common multiplayer-->there is no common multiplayer
so exit from the loop
return 2*3*m1*m2
ie, return 2*3*2*5=60




"""
















# def lcm(m1,m2,g):
#     if g%m1==0 and g%m2==0:
#         return g
#     else:
#         return lcm(m1,m2,g+1)
# m1=int(input("enter the number:"))
# m2=int(input("enter the number:"))
# g=max(m1,m2)
# print(lcm(m1,m2,g))

