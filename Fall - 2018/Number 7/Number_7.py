"""
Weekly Challenge:
Write a function that rotates a list by k elements.
For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
"""


def rotate(lst, n):
   if n > len(lst):
      n = n % len(lst)
   x = lst[n::]
   y = lst[:n:]
   return x+y


rotate([1, 2, 3, 4, 5, 6], 2)
rotate([1, 2, 3, 4, 5, 6], 4)
