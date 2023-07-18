#Write a program to print multiplication table of a given number
n=int(input("enter the number of multiplicand"))
r=int(input("enter the range of multiplier"))
for i in range(1,r+1):
    print(i,"*",n,"=",i*n)