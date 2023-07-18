#   2.Write a Python program to reverse a string.
#Sample String: "1234abcd"
#Expected Output: "dcba4321"

def sum(str1):
    x=str1[::-1]
    return x
str1 = str(input("enter the string"))
print(sum(str1))