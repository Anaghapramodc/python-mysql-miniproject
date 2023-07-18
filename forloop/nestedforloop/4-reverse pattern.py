#Reverse pattern from 10 to 1
row=int(input("enter the rows"))
for i in range(0,row):
   for s in range(row-i,0,-1):
           print(s," ",end="")
   print()


























































"""
10  9  8  7  6  5  4  3  2  1  
9  8  7  6  5  4  3  2  1  
8  7  6  5  4  3  2  1  
7  6  5  4  3  2  1  
6  5  4  3  2  1  
5  4  3  2  1  
4  3  2  1  
3  2  1  
2  1  
1
"""

#Reverse pattern from 10 to 1
row=int(input("enter the rows"))
for i in range(0,row):
   for s in range(10-i,0,-1):
           print(s," ",end="")
   print()