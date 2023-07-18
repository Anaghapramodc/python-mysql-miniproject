#Write a program to separate negative and positive numbers from a given list ?(accept input from the user.)
r=int(input("enter the numbers of elements in the list"))
print("enter the numbers")
p=[]
n=[]
for i in range(r):
    x=int(input())
    if x>0:
        p.append(x)
    else:
        n.append(x)
print("possitive numbers are=",p)
print("negetive numbers are=",n)