str1="/*jon is 2developer $music director"
str2=""
for char in str1:
    if char.isalpha()==True or char.isspace()==True:
        str2=str2+char
print(str2)