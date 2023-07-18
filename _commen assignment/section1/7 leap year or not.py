y=int(input("enter the year"))
if y%400==0 :
    print(f"{y} is leap year")
elif y%4==0 and y!=100:
    print(f"{y} is leap year")
else:
    print(f"{y} is not leap year")