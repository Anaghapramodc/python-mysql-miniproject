#take 3 int values from useds and print greatest among them
x=int(input("Enter the first value"))
y=int(input("Enter the second value"))
z=int(input("Enter the thired value"))
if x>y and x>z:
    print(x, "is greater ")
elif y>x and y>z:
    print(y," is greater ")
elif z>x and z>y:
    print(z," is greater ")
elif x==y and x!=z:
    print("first and second are greater ")
elif y==z and x!=y:
    print("second and thired are greater ")
elif x==z and x!=y:
    print("first and thired are greater ")
else:
    print("all are equal")
