#to print the character of letter of your name
#A

row=int(input("enter the rows"))
for i in range(1, row+1):
    for b in range(0, row-i):
        print(" ", end=" ")
    for c in range(0, i+1):
        if c==0 or c==i:
            print("*", end=" ")
        elif i==6 and c<6 :
            print("*","*",end=" ")
        else:
              print("   ",end=" ")
    print()











































"""
                  * * 
                *     * 
              *         * 
            *             * 
          *                 * 
        * * * * * * * * * * * * 
      *                         * 
    *                             * 
  *                                 * 
*                                     * 
"""
# row=int(input("enter the rows"))
# for i in range(1, row+1):
#     for b in range(0, row-i):
#         print(" ", end=" ")
#     for c in range(0, i+1):
#         if c==0 or c==i:
#             print("*", end=" ")
#         elif i==6 and c<6 :
#             print("*","*",end=" ")
#         else:
#               print("   ",end=" ")
#     print()