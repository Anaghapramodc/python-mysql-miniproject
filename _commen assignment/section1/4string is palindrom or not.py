s1=str(input("enter the string"))
l1=list(s1.lower())
l2=l1.copy()
x=l2.reverse()
if l1==l2:
    print(f"{s1} is palindrom")
else:
    print(f"{s1} is not palindrom")