# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

a=int(input("Enter the mark ="))
if a>80:
    print("You got A Grade")
elif 60<a<=80:
    print("You got B Grade")
elif 50<a<=60:
    print("You got C Grade")
elif 45<a<=50:
    print("You got D Grade")
elif 25<=a<=45:
    print("You got E Grade")
else:
    print("You Are Failed")