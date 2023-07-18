#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("Enter your salary ="))
year=int(input("Enter the year of experience="))
if year>5:
    bonus=salary*(5/100)
    print("you are eligible for bonus \n" ," bonus amount =",bonus,"\n corrent salary=",salary+bonus)
else:
    print("you are not eligible for bonus\n","bonus amount =0\n","corrent salary=",salary)
