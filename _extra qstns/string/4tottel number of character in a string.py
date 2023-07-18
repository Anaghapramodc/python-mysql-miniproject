#Count the total number of characters in a string
s=str(input("enter the string"))
s1=""
for i in s:
    if i==" ":
        continue
    else:
         s1=s1+i
print(len(s1))
