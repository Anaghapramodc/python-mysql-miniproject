"""
*  *  *  *  *
 *  *  *  *
  *  *  *
   *  *
    *
    *
   *  *
  *  *  *
 *  *  *  *
*  *  *  *  *

"""
#assignment11
row=int(input("enter the rows"))
for i in range(row, 0, -1):
    for b in range(0, row-i):
        print(" ", end=" ")
    for c in range(1, i+1):
        print("*  ", end=" ")
    print()
for j in range(1, row+1):
    #print(i)
    for d in range(0, row-j):
        print(" ", end=" ")
    for x in range(1, j+1):
        print("*  ", end=" ")
    print()
