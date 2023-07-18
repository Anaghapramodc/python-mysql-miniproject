"""
1)array
linear data strucure
it contain group of elements
all elements are same data type(int or str)
each elements in an array has a numerical index which is use to identify elements
each datas are stored in a continues memory location

one dimentional array
the array with on e subscript that array is called as one dimentional array.
int a[5];
two dimentional array
the array with two subscript that array is called as two dimentional array.
int a[5][5];
multi dimentional array
the array with more than two subscript that array is called as multi dimentional array

array representaion

basic operations
traverse:-print all elements one by one
insertion:-add an element at a given intex
deletion:-delete an element in a given intex
search:-search an element using given intex
update :-update an element at the given intex

from array import* #array is created by importing array module
arrayname=array(typecode,[initializers])

typecode:-the code which represent the type of the values
type code	python type	       minimum size in bytes
 'b'	       int	                    1
 'B'	       int	                    1
 'u'	  unicode character	            2
 'h'	       int	                    2
 'H'	       int	                    2
 'i'	       int	                    2
 'I'	       int	                    2
 'l'	       int	                    4
 'L'	       int	                    4
 'q'	       int	                    8
 'Q'	       int	                    8
 'f'	      float	                    4
 'd'	      float	                    8

"""

from array import*
array1=array('i',[1,2,3,4,5,6,7])
for x in array1:
    print(x)
print(array1[0])
print(array1[4])

from array import*
array1=array('u',['a','b','c','d','e','f'])
for x in array1:
    print(x)
print(array1[0])
print(array1[4])

from array import*
array1=array('f',[1,1.5,2,2.5,3,3.5])
for x in array1:
    print(x)
print(array1[0])
print(array1[4])