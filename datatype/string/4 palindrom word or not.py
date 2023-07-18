s=str(input("enter the string"))
s=s.lower()
s1=s[::-1]
if s==s1:
    print(f"{s} is palindrome ")
else:
    print(f"{s} is not palindrome")