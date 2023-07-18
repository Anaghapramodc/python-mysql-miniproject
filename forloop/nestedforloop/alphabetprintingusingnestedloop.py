"""
to print alphabets A to Z
A-65       a-97
Z-90       z-122

use chr()
"""
# for i in range(65,91):
#     print(chr(i)," ",end="")
# print()
# for i in range(97,123):
#     print(chr(i)," ",end="")

"""
A  
B  C  
D  E  F  
G  H  I  J  
K  L  M  N  O  
"""
# row=int(input("enter the rows"))
# a=65
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(chr(a) ," ", end="")
#         a=a+1
#     print()
"""
          A   
        B   C   
      D   E   F   
    G   H   I   J   
  K   L   M   N   O   



"""
# row = int(input("enter the rows"))
# a=65
# for i in range(0,row):
#     #print(i)
#     for b in range(0,row-i):
#         print(" ", end=" ")
#     for c in range(0, i+1):
#         print(chr(a)," ", end=" ")
#         a=a+1
#     print()
"""
Z  Y  X  W  V  
U  T  S  R  
Q  P  O  
N  M  
L  
"""
row=int(input("enter the rows"))
a=90
for i in range(0,row+1,):
   for s in range(1,row+1-i):
       print(chr(a)," ",end="")
       a=a-1
   print()
"""
A  B  C  D  E  
F  G  H  I  
J  K  L  
M  N  
O 
"""
row=int(input("enter the rows"))
a=65
for i in range(0,row+1,):
   for s in range(1,row+1-i):
       print(chr(a)," ",end="")
       a=a+1
   print()

"""
A   B   C   D   E   
  F   G   H   I   
    J   K   L   
      M   N   
        O 



"""

row=int(input("enter the rows"))
a=65
for i in range(row, 0, -1):
    #print(i)
    for b in range(0, row-i):
        print(" ", end=" ")
    for c in range(0, i):
        print(chr(a)," ", end=" ")
        a=a+1
    print()