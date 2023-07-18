
"""
     * i=10-->s=0,1,2,3,4-->*1
    *** i=8-->s=0,1,2,3-->*1,2,3
   ***** i=6-->s=0,1,2-->*1,2,3,4,5
  ******* i=4-->s=0,1-->*1,2,3,4,5,6,7
 ********* i=2-->s=0-->*1,2,3,4,5,6,7,8,9


"""
# row=int(input("enter the rows"))
# for i in range(row,0,-2):
#     for s in range(0,int(i/2)):
#        print("v",end="")
#     for j in range(0,row-i+1):
#        print("*",end="")
#     print()

"""
 *******************
  *****************
   ***************
    *************
     ***********
      *********
       *******
        *****
         ***
          *
"""


# row=int(input("enter the rows"))
# for i in range(2,2*row+1,2):
#     for s in range(int(i/2),0,-1):
#        print(" ",end="")
#     for j in range(0,2*row-i-1+2):
#        print("*",end="")
#     print()









"""
   *****     ***** i=6-->s=0,1,2-->*0,1,2,3,4   
  *******   ******* i=4-->s=0,1-->*0,1,2,3,4,5,6
 ********* ********* i=2-->s=0-->*0,1,2,3,4,5,6,7,8
 ******************* i=2-->s=1-->*19
  ***************** i=4-->s=1,2-->17
   *************** i=6-->s=1,2,3-->15
    ************* i=8-->s=1,2,3,4-->13
     *********** i=10-->s=1,2,3,4,5-->11
      ********* i=12-->s=1,2,3,4,5,6-->9
       ******* i=14-->s=1,2,3,4,5,6,7-->7
        ***** i=16-->s=1,2,3,4,5,6,7,8-->5
         *** i=18-->s=1,2,3,4,5,6,7,8,9-->3
          * i=20-->s=1,2,3,4,5,6,7,8,9,10-->1
"""
#heart shape
row=int(input("enter the rows"))
for i in range(row,0,-2):
    if i==10 or i==8 :
            continue
    for s in range(0,int(i/2)):
       print(" ",end="")
    for j in range(0,row-i+1):
       print("*",end="")
    for d in range(0,i-1):
        print(" ", end="")
    for k in range(0, row - i +1):
        print("*", end="")
    print()
for i in range(2,2*row+1,2):
    for s in range(int(i/2),0,-1):
       print(" ",end="")
    for j in range(0,2*row-i+1):
       print("*",end="")
    print()
"""
      * * * * *           * * * * * 
    * * * * * * *       * * * * * * * 
  * * * * * * * * *   * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * 
        * * * * * * * * * * * * * 
          * * * * * * * * * * * 
            * * * * * * * * * 
              * * * * * * * 
                * * * * * 
                  * * * 
                    * 

"""
# heart shape with space
row=int(input("enter the rows"))
for i in range(0,row,2):
    if i==0 or  i==1 or i==2:
            continue
    for s in range(0,row-i):
       print(" ",end="")
    for j in range(1,i+2):
       print("* ",end="")
    for d in range(1,2*(row-i)-1):
        print(" ", end="")
    for k in range(1,i+2):
        print("* ", end="")
    print()
for i in range(2*row+1,0,-2):
    for s in range(0,2*row-i+3):
       print(" ",end="")
    for j in range(3,i+1):
       print("* ",end="")
    print()



