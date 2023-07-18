str1="hello"
str2="world"
c=len(str1)
print(f"{str1[:int(c/2)]}{str2}{str1[int(c/2):]}")