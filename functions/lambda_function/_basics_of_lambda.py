""""
function in single line
signle expresion only possible
not allow multiple opperation

syntax

lambda arguments():expresion
"""

x=lambda a: a+10
print(x(5))

y=lambda a,b,c:a+b+c
print(y(1,2,3))



z=lambda x=1: print("anagha")
z(1)
tuple=[('english',88),('science',90),('maths',98),('social science',77)]
tuple.sort(key=lambda a:a[0])
# print(tuple)

#program to sort list of dictionary using lambda
# dict={'english':66,'maths':98,'physics':84,'biology':76}
# print(list(dict))
# # list(dict).sort(key=lambda a:)
