"""
Make a function that takes a list and returns the list sorted using selection sor
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
The algorithm maintains two subarrays in a given array.
"""


def selectionSort(unsortedList):
    lst = unsortedList[::]
    for i in range(len(lst)):
        temp = i
        for j in range(i, len(lst)):
            if lst[temp] > lst[j]:
                temp = j

        lst[i], lst[temp] = lst[temp], lst[i]
    return lst

print(selectionSort([2, 1, 54, 5, 345, 3, 45, 13, 21, 3]))
print(selectionSort([0, 2, 89, 3, 6, 57, 65, 76, 57, 653, 4546, 43]))
