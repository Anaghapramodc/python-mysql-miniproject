#accept 10 numbers from the user and display there average
sum=0
print("enter the numbers")
for i in range(1,11):
    n=int(input(""))
    sum=sum+n
avg=sum/10
print("average of numbers =",avg)
