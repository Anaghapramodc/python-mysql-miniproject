""""
dictionary
dictionaries are used to store data values are in key:value pairs.
mutable
indexed by keys
ordeded
duplicates not allowed
"""

dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
# print(dict1)
# print(dict1["name"])
# print(len(dict1))
# x="anagha"
# d1={x}
# print(d1)

#methords in dictionary
#get()
x=dict1.get("name")#to access the the value of the key
print(x)
#key()
print(dict1.keys())#to print all the key words
#values()
print(dict1.values())#to print all the values of key word
#clear()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict1.clear()#to clear the dictionary
print(dict1)
#copy
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
x=dict1.copy()#to coppy a dictionary
print(x)
#items()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
x=dict1.items()#to seperate all items in the dictionary
print(x)
print("\n")
#pop()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict1.pop("name")#to remove the keyword and its value
print(dict1)
# #popitem()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict1.popitem()#to remove the last keyword
print(dict1)
# #update()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict1.update({"batch":"3rd"})#to update keywords and values
print(dict1)
print("\n")
 #setdefault()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict1.setdefault("batch")#to add keywords and  values in a dictionary
print(dict1)
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict1.setdefault("batch",3)
print(dict1)
# #fromkeys()
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
z="error"
t=dict1.fromkeys(dict1,z)#use to change all values of keywords in to aperticular value
print(t)
dict2={1,2,3,4,5,5}
x="hai"
y=dict1.fromkeys(dict2,x)
print(y)
dict1={"name":"anagha","age":22,"place":"kuthuparamba","course":"python"}
dict2={1,2,3,4,5,5}
x=[11,22,33,44,55,55]
y=dict1.fromkeys(dict2,x)
print(y)
dict2={1,2,3,4,5,5}
y=dict1.fromkeys(dict2,0)
print(y)


