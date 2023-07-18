str1="p@#$yn26at^i5ve"
str2=""
str3=""
str4=""
for char in str1:
    if char.isalpha():
        str2=str2+char
    elif char.isdigit():
        str3 = str3 + char
    else:
         str4=str4+char
print(f"the string contains {len(str2)} alphabets")
print(f"the string contains {len(str3)} digits")
print(f"the string contains {len(str4)} spacial characters")