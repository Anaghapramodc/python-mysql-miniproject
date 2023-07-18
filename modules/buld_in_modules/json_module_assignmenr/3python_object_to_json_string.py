#convert python object to json string print all value
import json
s={'name':'anagha','place':'kuthuparamba'}
y=json.dumps(s)
print(y)
print(type(y))
print(y[0::])
