def rotate(lst, n):
   if n > len(lst):
      n = n % len(lst)
   x = lst[n::]
   y = lst[:n:]
   return x+y

rotate([1, 2, 3, 4, 5, 6], 2)