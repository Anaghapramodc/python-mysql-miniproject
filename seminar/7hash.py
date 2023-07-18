"""
heap
1)heap is a special tree structure
2)each parant node is lessthan or equal to the child node it is called min node
3)each parant node i greater than or equal to the child node it is called max node
4)heap is created by using inbuilt library named heapq
5)functions to carry out various operatuins on heap data structure
   heapify:-this function convert a regular list to a heap.
   heappush:-this function adds an element to the heap without altering the current heap.
   heappop:- this function returns the smallest element from the heap.
   heapreplace:- this function replaces the smallest data with a new value supplied in the function.

"""
import heapq
h=[5,12,33,45,7]
heapq.heapify(h)
print(h)