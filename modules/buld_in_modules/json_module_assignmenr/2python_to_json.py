#convert python objrct to json
import json
s={'name':'anagha','place':'kuthuparamba',}
y=json.dumps(s)
print(y)
print(type(y))

x='[1,2,3,4]'
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))

x=(1,2,3,4)
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))