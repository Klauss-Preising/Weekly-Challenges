"""
Weekly Challenge week 6:
I want you guys to sort a list using Bubble Sort.
Bubble sort, compares each pair of adjacent items and swaps them if they are in the wrong order.
"""

def bubbleSort(unsorted_lst):
    lst = unsorted_lst[::]
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst

print(bubbleSort([6,7,4,1,2,5,3]))
print(bubbleSort([0, 2, 89, 3, 6, 57, 65, 76, 57, 653, 4546, 43]))
