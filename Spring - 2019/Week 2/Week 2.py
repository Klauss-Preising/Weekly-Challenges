"""
Week 2:
Given two arrays of ints sorted in increasing order, outer and inner, return true if all of the numbers in inner appear in outer.
The best solution makes only a single "linear" pass of both arrays, taking advantage of the fact that both arrays are already in sorted order.

linearIn([1, 2, 4, 6], [2, 4]) → true
linearIn([1, 2, 4, 6], [2, 3, 4]) → false
linearIn([1, 2, 4, 4, 6], [2, 4]) → true
"""


# function by Klauss
def linearIn_klauss(lst1, lst2):
    j = 0
    i = 0
    while(j < len(lst2) and i < len(lst1)):
        if lst1[i] > lst2[j]:
            return False
        if lst1[i] == lst2[j]:
            j += 1
        i += 1
    return j >= len(lst2)

# function by David
def linearIn_david(outer, inner):
    if (all(i in outer for i in inner)):
        return True
    else:
        return False

# function by George
def linearIn_george(outer, inner):
    if len(inner) == 0:
        print(True)
    elif len(outer) == 0:
        print(False)
    elif inner[0] == outer[0]:
        linearIn_george(outer[1:], inner[1:])
    else:
        linearIn_george(outer[1:], inner)

# Function by Thahera
def linearIn_thahera(outer, inner):
    ans = True
    outLen = len(outer)
    inLen = len(inner)
    if inLen > outLen:
        return False
    for element in inner:
        if element in outer:
            ans = True
        else:
            ans = False
            break
    return ans
