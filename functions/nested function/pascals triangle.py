# Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
"""
     1
   1    1
  1   2   1
 1   3   3   1
1  4   6  4   1
"""

""" 
               (0,0)
            (1,0),(1,1)
         (2,0),(2,1),(2,2)
      (3,0),(3,1),(3,2),(3,3)
   (4,0),(4,1),(4,2),(4,3),(4,4)
(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)

"""
def fact(n):
     p=1
     for i in range(1,n+1):
         p=p*i
     return p
n=int(input("enter the number"))
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end="  ")
    for j in range(i + 1):
        # iCj = i!/((i-j)!*j!)
        print(fact(i) // (fact(j) * fact(i-j)), end="   ")
    # for new line
    print()






