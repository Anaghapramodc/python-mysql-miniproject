#convert json encoded data to python object
import json
x='[1,2,3,45]'
y=json.loads(x)
print(y)
print(type(y))

x='1234'
print(type(x))
y=json.loads(x)
print(y)
print(type(y))

x='[1,2,3,4]'
print(type(x))
y=json.loads(x)
print(tuple(y))
print(type(y))