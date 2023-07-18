"""
        *
      *    *
    *        *
  *            *
*                *
  *            *
    *        *
      *    *
        *
"""
#diamond pattern
row=int(input("enter the rows"))
for i in range(0, row):
    #print(i)
    for b in range(1, row-i):
        print(" ", end=" ")
    for c in range(0, i+1):
        if c==0 or c==i:
            print("*  ", end=" ")
        else:
            print("   ", end=" ")
    print()
for i in range(row-1, 0, -1):
#     #print(i)
    for b in range(1, row-i+1):
        print(" ", end=" ")
    for c in range(0, i):
        if c==0 or c==i-1:
            print("*  ", end=" ")
        else:
            print("   ", end=" ")
        # print(c," ", end=" ")
    print()

