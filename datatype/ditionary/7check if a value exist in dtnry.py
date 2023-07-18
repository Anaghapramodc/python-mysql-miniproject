#check if a value exist in a dictionary
dict1={"name":"anagha","age":22,"course":"python","batch":3,"time":"9am"}
x=input("enter the value:")
for i in dict1:
    if x == dict1.get(i):
        print(f"{x} is exist in the dictionary")
        break
else:
    print(f"{x} is not exist in the dictionary")