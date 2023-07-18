#convert json data to python object
import json
s='{"name":"anagha","course":"python"}'
t=json.loads(s)
print(t)
print(type(t))