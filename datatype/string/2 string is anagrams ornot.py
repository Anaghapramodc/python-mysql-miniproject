"""
anagram strings-->race care
                  heart earth
                  sadder dreads
"""
str1=str(input("enter the first string"))
str2=str(input("enter the second string"))
c=0
for char1 in str1:
    for char2 in str2:
       if char1==char2:
          c=c+1
          break
if c==len(str1)==len(str2):
    print(f"{str1} and {str2} are anagrams ")
else:
    print(f"{str1} and {str2} are not anagrams ")
