#create a dictionary by extracting the keys from a given dictionary
dict1={"name":"anagha","age":22,"course":"python","batch":3,"time":"9am"}
dict2={}
for i in dict1:
    dict2.setdefault(i)
print(dict2)
