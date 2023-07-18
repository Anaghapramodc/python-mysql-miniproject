""""
enter the number 5


      *5
    *  *4
   *  *  *3
  *  *  *  *2
 *  *  *  *  *1
*  *  *  *  *  *0
 *  *  *  *  *1
  *  *  *  *2
   *  *  *3
    *  *4
      *5
"""


#1.try to creat diamond pattern
row = int(input("enter the rows"))
for i in range(0,row+1):
    #print(i)
    for b in range(0,row-i):
        print(" ", end=" ")
    for c in range(0, i+1):
        print("*  ", end=" ")
    print()
for j in range(row, 0, -1):
    #print(i)
    for d in range(0, row-j+1):
        print(" ", end=" ")
    for a in range(0, j):
        print("*  ", end=" ")
    print()

