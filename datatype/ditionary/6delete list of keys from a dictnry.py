#delete a list of keys from a dictionary
dict1={"name":"anagha","age":22,"course":"python","batch":3,"time":"9am","colour":"red","vehicle":"car"}
list1=["name","age","colour","vehicle"]
for i in list1:
    dict1.pop(i)
print(dict1)