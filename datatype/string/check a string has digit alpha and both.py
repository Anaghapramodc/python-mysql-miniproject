# s=str(input("enter the string"))
# x1=""
# for char in s:
#     if char!=" ":
#        x1=x1+char
# if x1.isalpha()==True:
#     print("the string only contains alphabets")
# elif x1.isdigit()==True:
#     print("the string only contains digits")
# elif x1.isalnum()==True:
#     print("the string contains alphabets and digits")
# else:
#     print("the string contains special characters")

s=str(input("enter the string"))
x1=""
for char in s:
    if char != " ":
     x1=x1+char
if x1.isalnum()==True and x1.isalpha()==False and x1.isdigit()==False :
        print("true")
else:
        print("false")

