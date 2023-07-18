#cross patern of number

row=int(input("enter the rows"))
for i in range(1,2*row):
    for b in range(1,2*row):
        if( i==b<6) or i+b==9 and i<5:
            print(i, end=" ")
        if (i == b >= 6) :
            print(10-b, end=" ")
        if i + b == 10 and i >= 6:
            print(b, end=" ")

        else:
            print(" ",end=" ")
    print()














"""""
1               1     
  2           2       
    3       3         
      4   4           
        5           
      4   4         
    3       3       
  2           2     
1               1   



"""