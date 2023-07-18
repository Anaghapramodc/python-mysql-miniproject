"""
3)stack
used to store collection of object
individual items can added and stored in a stackusing push operaters
the element may be inserted or deleted only at one end called top of thr stack

last in first out(LIFO)
the element inserted in last in the sequence will come out first
we can remove only at the top of the stack
push pop are the adding and removeing functions.




"""

def stack():
    s=[]
    r=int(input("enter the range of stack:"))
    for i in range(r):
        e=input("enter the element:")
        s.pop()