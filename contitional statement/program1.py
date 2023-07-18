a=int(input("enter the value"))
if a%7==0 and a%5==0:
    print(a,"is divisible by 7 and multiple by 5")
elif a%7==0:
    print(a,"is divisible by 7 and not a multiple by 5")
elif a%5==0:
    print(a,"is not divisible by 7 but it is a multiple by 5")
else:
    print(a,"is not devisible by 7 and not multiple by 5")

