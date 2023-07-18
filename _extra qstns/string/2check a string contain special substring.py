str1=str(input("enter the string"))
x=str1.upper()
sub1=str(input("enter the sub string"))
y=sub1.upper()
if y in x:
    print(f"{sub1} is a substring of {str1}")
else:
    print(f"{sub1} is not substring of {str1}")