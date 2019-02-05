"""
Week 1:
For each multiple of n in the given array, change all the values following it to be that multiple of n, until encountering another multiple of n.

Example:
multiple(10, [2, 10, 3, 4, 20, 5]) → [2, 10, 10, 10, 20, 20]
multiple(5, [10, 1, 20, 2]) → [10, 10, 20, 20]
multiple(3, [10, 1, 9, 20]) → [10, 1, 9, 9]
"""

def multiple(n, lst):
    temp = lst[0]
    lst_ = lst[::]
    for i in range(1, len(lst_)):
        if (lst_[i] % n) == 0:
            temp = lst_[i]
        elif temp % n == 0:
            lst_[i] = temp
    return lst_

print(multiple(10, [2, 10, 3, 4, 20, 5]))
print(multiple(5, [10, 1, 20, 2]))
print(multiple(3, [10, 1, 9, 20]))
