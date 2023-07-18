#Count the number of a specific character in a string
s=str(input("enter the string"))
s1=s.lower()
print(s1)
a=str(input("enter the special character"))
a1=a.lower()
print(a1)
c=0
for i in s1:
    if i==a1:
        c=c+1
print(f"the special character {a} is repeating {c} times")

