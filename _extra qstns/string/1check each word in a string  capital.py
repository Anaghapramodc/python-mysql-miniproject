w=str(input("enter the string"))
for i in w:
    if i.isupper():
        pass
    else:
        print(f"the string {w} contains lower letter")
        break
else:
    print(f"all letters in the string {w} are capital")