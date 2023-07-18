""""
module
when we have to access function which is defined in other py file

from file name import function name
"""
from example import sum
print(sum(2,3))

from example import sqr
sqr(5,4)

from example import sum
print(sum(2,35))
#when the function is defined on another directory

from functions.square_value import sqr
sqr(2,3)
