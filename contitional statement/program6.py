#take 3 int values from useds and print greatest among them using nested if
x=int(input("Enter the first value"))
y=int(input("Enter the second value"))
z=int(input("Enter the thired value"))
if x>y and x>z:
    print(x, "is greater ")
elif y>x and y>z:
    print(y," is greater ")
elif z>x and z>y:
    print(z," is greater ")
elif x==y:
    if x!=z and x>z:
        print("first and second are equal ")
    else:
        print("all are equal")
elif y==z:
    if y!=x and y>x:
        print("second and thired are equal ")
elif x==z:
    if z!=y and z>y:
        print("first and thired are equal")

