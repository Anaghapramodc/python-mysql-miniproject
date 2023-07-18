def lsearch(r, x):
   for i in range(len(r)):
      if r[i] == x:
         return i
   return -1
r= [1,22,3,4,5,11,2,3,54]
x = 11
print("element found at index ",lsearch(r,x))
print("antinna")
