#nested  for loop
"""
for(i in range()):
    for i in range():
"""

#full peramid
"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""

# row = int(input("enter the rows"))
# for i in range(0,row):
#     #print(i)
#     for b in range(0,row-i):
#         print(" ", end=" ")
#     for c in range(0, i+1):
#         print("*  ", end=" ")
#     print()
"""
    * 
  * * * 
* * * * * 
"""
# row=int(input("enter the rows"))
# for i in range(0,row,2):
#    for s in range(0,row-i):
#        print("n",end="")
#    for j in range(1,i+2):
#        print("* ",end="")
#    print()

"""
*
* *
* * *
* * * *
* * * * *
"""

# row=int(input("enter the rows"))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("* "," ", end="")
#     print()
"""
* * * * *      
* * * * 
* * * 
* * 
*
"""
# row=int(input("enter the rows"))
# for i in range(0,row+1,):
#    for s in range(1,row+1-i):
#        print("*  ",end="")
#    print()
"""
* * * * * 
 * * * *  
  * * *
   * *
    *   
"""
# row=int(input("enter the rows"))
# for i in range(row, 0, -1):
#     #print(i)
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(0, i):
#         print("*  ", end=" ")
#     print()



"""
      1 
     1 1 
    1 * 1  
   1 * * 1 
  1 * * * 1
 1 * * * * 1 



"""
# row=int(input("enter the rows"))
# for i in range(0, row+1):
#     #print(i)
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(0, i+1):
#         if c==0 or c==i:
#             print("1  ", end=" ")
#         else:
#             print("*  ", end=" ")
#     print()
"""
      1 
     1  2
    1  2  3  
   1  2  3  4 
  1  2  3  4  5
 1  2  3  4  5  6 
# """
# row=int(input("enter the rows"))
# for i in range(0, row+1):
#     #print(i)
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(1, i+1):
#          print(c,"  ", end=" ")
#     print()


"""
      1 
     1 1 
    1 2 1  
   1 3 3 1 
  1 4 6 4 1
1 5 10 10 5 1 
"""
"""
row=int(input("enter the rows"))
for i in range(0, row+1):
    #print(i)
    for b in range(0, row-i):
        print(" ", end=" ")
    for c in range(0, i+1):
        if c==0 or c==i:
            print(" 1 ", end=" ")
        else:
            print("", end=" ")
        if c!=0 and c!=i:
        #     for d in range(1,row-1):
        #         pass
          print("2 ", end=" ")


"""
#
# row=int(input("enter the rows"))
# f=1
# for i in range(0, row+1):
#     #print(i)
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(0, i+1):
#          if c==i or c==0:
#              print( "1  ", end=" ")
#          elif c==1:
#               print(f,"  ",end="")
#               f=f+1
#          elif c==2:
#              print(f,"  ",end="")
#              f=f+2
#
#     print()
"""
1
1  2
1  2  3
1  2  3  4
1  2  3  4  5
1  2  3  4  5  6
"""
# row=int(input("enter the rows"))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,"  ", end="")
#     print()
"""
1  2  3  4  5
1  2  3  4
1  2  3
1  2
1
"""
# row=int(input("enter the rows"))
# for i in range(0,row+1,):
#    for s in range(1,row+1-i):
#        print(s,"  ",end="")
#    print()

"""
      1 
     1 1 
    1 2 1  
   1 2 2 1 
  1 2 3 2 1
 1 2 3 3 2 1 



"""
#
# row=int(input("enter the rows"))
# for i in range(1, row+1):
#     #print(i)
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(1, i+1):
#         if c==1 or c==i:
#             print("1 ", end=" ")
#         if c>1 and c<i:
#             for d in range(2,i):
#                 if c==d:
#
#                   print(d," ", end=" ")
#             # c=c+i
#             # print(c," ", end=" ")
#     print()














"""
1  2  3  4  5 
 1  2  3  4 
  1  2  3
   1  2   
    1  
    1 
   1  2
  1  2  3  
 1  2  3  4 
1  2  3  4  5




"""
# row=int(input("enter the rows"))
# for i in range(row, 0, -1):
#     #print(i)
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(1, i+1):
#         print(c,"  ", end=" ")
#     print()
# for j in range(0, row+1):
#     #print(i)
#     for d in range(0, row-j):
#         print(" ", end=" ")
#     for x in range(1, j+1):
#          print(x,"  ", end=" ")
#     print()


row=int(input("enter the rows"))
for i in range(row,0,-2):
    for s in range(0,row-i+1):
        print("4",end="")
    for j in range(0,i+1):
       print("*",end="")
    print()
