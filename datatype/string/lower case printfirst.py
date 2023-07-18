str1="HeLLO World"
c=len(str1)
str2=""
str3=""
for char in str1:
    if char.islower():
        str2=str2+char
    if char.isupper():
        str3 = str3 +char
print(f"{str2}{str3}")