
""""
x='{"name":"anagha,"age":22}' #gson object
dictionary-object
list-array
null-non
int-number
str-str
"""
import json
print(dir(json))
#passing
#convert python to json
#dums used to convert
x={"name":"anagha","age":22}
y=json.dumps(x)
print(y)
print(type(y))

#conver json to python
#loads sed to convert
x='{"name":"anagha","age":22}'
y=json.loads(x)
print(y)
print(type(y))

x=[1,2,3,45]
y=json.dumps(x)
print(y)
print(type(y))

x=2.345
y=json.dumps(x)
print(y)
print(type(y))
