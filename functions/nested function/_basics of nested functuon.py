"""
nested function
def outer_fun():
     def inner_fun():
       print("hai dear")
     inner_fun()
  outer_fun()
"""

def number(num):
    def count():
         return num+1
    return count()
print(number(10))

def number(num):
    def count():
        return num+1
    return count()
print(number(10))
