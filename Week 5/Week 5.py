"""
Weekly Challenge Week 5:
I want you guys to sort sort a list using Insertion sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by putting the element in the proper position
"""


def insertionSort(x):
    temp = [x[0]]

    for i in range(1, len(x)):
        temp2 = len(temp)
        for j in range(temp2):
            if x[i] < temp[j]:

                temp.insert(j, x[i])
                break
        if temp2 == len(temp):
            temp.append(x[i])
        print (temp, x)
    return temp



print(insertionSort([6,7,4,1,2,5,3]))
print(insertionSort([0, 2, 89, 3, 6, 57, 65, 76, 57, 653, 4546, 43]))