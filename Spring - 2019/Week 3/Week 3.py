"""
Week 3:
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target,
with this additional constraint: if there are numbers in the array that are adjacent and the identical value,
they must either all be chosen, or none of them chosen. For example, with the array {1, 2, 2, 2, 5, 2},
either all three 2's in the middle must be chosen or not, all as a group.
(one loop can be used to find the extent of the identical values).


groupSumClump(0, [2, 4, 8], 10) → true
groupSumClump(0, [1, 2, 4, 8, 1], 14) → true
groupSumClump(0, [2, 4, 4, 8], 14) → false
"""


# start: will be the starting position or index of the list
# lst: the list
# target: the sum target i'm looking for
def groupSumClump_klauss(start, lst, target):
    if start >= len(lst):   # base case
        return target == 0

    # th
    i = start
    sum = 0
    while i < len(lst) and lst[start] == lst[i]:
        sum += lst[i]
        i += 1

    if groupSumClump_klauss(i, lst, target - sum):
        return True

    if groupSumClump_klauss(i, lst, target):
        return True
    return False


print(groupSumClump_klauss(0, [2, 4, 8], 10))
print(groupSumClump_klauss(0, [1, 2, 4, 8, 1], 14))
print(groupSumClump_klauss(0, [2, 4, 4, 8], 14))

# Author: Georgios Karakyklas

# helper function that removes adjacent duplicates
def consecutive(lst):
    # loop through all elements of the list, except the first
    for i in range(1, len(lst)):
        # check if the i element is a duplicate of the previous
        if lst[i] == lst[i - 1]:
            # add current element to previous
            lst[i - 1] += lst[i]
            # check if the next element is not the last or equal to the next
            if i + 1 < len(lst) and lst[i] != lst[i + 1]:
                lst[i] = 0
            # check if current element is the last
            elif i == len(lst) - 1:
                lst[i] = 0
    # return list
    return lst


def groupSumClump_georgios(start, lst, trgt):
    # check if length of list is smaller than start and target is not 0
    if start >= len(lst):
        return trgt == 0
    # check if increasing start and subtracting the previous number from target gets to closer to 0
    elif groupSumClump_georgios(start + 1, lst, trgt - lst[start]):
        return True
    # if previous number of list was too big, skip it
    elif groupSumClump_georgios(start + 1, lst, trgt):
        return True
    else:
        return False


print("groupSumClump(0, consecutive([2, 4, 8]), 10) →", groupSumClump_georgios(0, consecutive([2, 4, 8]), 10))
print("groupSumClump(0, consecutive([1, 2, 4, 8, 1]), 14) →", groupSumClump_georgios(0, consecutive([1, 2, 4, 8, 1]), 14))
print("groupSumClump(0, consecutive([2, 4, 4, 8]), 14) →", groupSumClump_georgios(0, consecutive([2, 4, 4, 8]), 14))


def groupSumClump_charlie(start, lst, target):
    if start >= len(lst):
        return target == 0
    temp = start
    adjSum = 0

    # conditional for if adjacent numbers are the same
    while (temp < len(lst) and lst[start] == lst[temp]):
        adjSum += lst[temp]
        temp += 1

    if (groupSumClump_charlie(temp, lst, target - adjSum)):
        return True

    if (groupSumClump_charlie(temp, lst, target)):
        return True

    return False


print(groupSumClump_charlie(0, [2, 4, 8], 10))
print(groupSumClump_charlie(0, [1, 2, 4, 8, 1], 14))
print(groupSumClump_charlie(0, [2, 4, 4, 8], 14))
