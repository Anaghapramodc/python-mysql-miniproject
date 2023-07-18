#Write a program to display all prime numbers within a range
# n=int(input("enter the number"))
# if n>0:
#     for i in range(2,n):
#         d=n%i
#         if d==0:
#
#             break
#     if d==0:
#         print(n,"is not a prime number")
#     else:
#         print(n,"is a prime number")
# else:
#     print("the number is rong")

# Write a program to display all prime numbers within a range
# r=int(input("enter the range of the prime number"))
# x=0
# if r>1:
#     print("prime numbers are")
#     for i in range(2,r+1):
#         for j in range(1,r+1):
#              d=i%j
#              if d==0:
#                  x=x+1
#         if x==2:
#             print(i)
#         x=0
# elif(r==1):
#     print("there is no prime number")
# else:
#     print("range is rong")

#simple methord
r = int(input("enter the range of the prime number"))
for i in range(2,r+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)



