import json
x={"name":"anagha","age":22,"couser":"python","place":"kpba","address":"xyz"}
y=json.dumps(x,sort_keys=True,indent=4)
print(y)
print(type(y))
print(y[4])