# Input:
# 1) array with indexes in a range of [0..n-1]
# array needs to be sorted, so:
# array[0] <= array[1] <= ... <= array[n-1]
#
# 2) we also need X, so the value we search for

# Output:
# inde of the element in the array, so the one where
# array[index] == X
# of course if X exists in the array
# otherwise "NO ELEMENT"


def binary_search(arr, X):
    # default binary search, "two comparisons"
    # time complexity: O(log n)
    L = 0
    R = len(arr)-1
    found = False
    midpoint = - 1
    while R - L >= 0 and not found:
        midpoint = (L+R)//2
        if X == arr[midpoint]:
            found = True
            break
        else:
            if X < arr[midpoint]:
                R = midpoint-1
            else:
                L = midpoint + 1
    if found:
        return midpoint
    else:
        return "no element"


# binary search after some modifications

# L algorithm
def lowerbound(arr, X):
    # L algorithm, also called lowerbound
    # time complexity: O(log n)
    # if X exists in the array, then the algorithm
    # finds its first occurence
    #
    # what if X does not exist in the array?
    # then the algorithm finds the next,
    # smallest element among the bigger ones than X
    # that exist in the array
    #
    # if X is bigger than the biggest element in the array,
    # then it points to the next element right after the end of an array
    #
    # that means, the algorithm finds the first position
    # that you can insert X at (while shifting the rest ones)
    # while making sure you don't break the order in the array
    L = 0
    R = len(arr)
    while L < R:
        midpoint = (L+R)//2  # floor
        if X <= arr[midpoint]:
            R = midpoint
        else:
            L = midpoint + 1
    return L


# R algorithm
def rightbound(arr, X):
    # L algorithm, also called rightbound
    # time complexity: O(log n)
    # if X exists in the array, then the algorithm
    # finds its last occurence
    #
    # what if X does not exist in the array?
    # then the algorithm finds the previous element,
    # so the biggest element among the smaller ones than X
    # that exist in the array
    #
    # if X is smaller than the smallest element in the array,
    # then it points to the element right before
    # the beginning of an array
    L = -1
    R = len(arr)-1
    while L < R:
        midpoint = (L+R+1)//2  # ceil
        if X < arr[midpoint]:
            R = midpoint - 1
        else:
            L = midpoint
    return L


# U algorithm
def upperbound(arr, X):
    # U algorithm, also called upperbound
    # time complexity: O(log n)
    # whether X exists in the array or not,
    # the algorithm finds the very first element
    # in the array that is bigger than X
    #
    # if X is bigger than the biggest element in the array,
    # then it points to the next element right after the end of an array
    #
    # that means, the algorithm finds the last position
    # that you can insert X at (while shifting the rest ones)
    # while making sure you don't break the order in the array
    L = 0
    R = len(arr)
    while L < R:
        midpoint = (L+R)//2
        if X < arr[midpoint]:
            R = midpoint
        else:
            L = midpoint + 1
    return L

# Observation:
# if the element does not exist in the array
# or the array is empty, then
# lowerbound and upperbound return the same values


# Based on the observation, we can use upperbound and lowerbound
# to count the number of occurences of a given value

# Next observation:
# naive solutions, like:
# 1) linear search
# 2) binary search to find the position of X in the array
#    and then to traverse the array in both directions
#    to count the occurences of X
#
# are all O(n) in the worst case.

# Can we do better?
# YES! The following expression:
# upperbound(arr, X)-lowerbound(arr, X)
# gives us the answer and the time complexity
# is still O(log n)

array = [0, 0, 1, 1, 1, 6, 11, 15]
print(upperbound(array, 1)-lowerbound(array, 1))  # 5 - 2 = 3
# value does not exist in the arr so 0
print(upperbound(array, 7)-lowerbound(array, 7))


# upperbound(array, X) - lowerbound(array, X)
# O(log n)          +      O(log n)
#            = O(log n)


# Second application of binary search:
# Solve the polynomial equation:
# W(x) = x^3 - 41x^2 - 34x -336 = 0
# we want to get the ceil of the value of the root p of this equation

# Assumptions:
# -100 < p < 1000
# W(-100)< 0
# W(1000) > 0

# We use the upperbound algorithm
def solve():
    L = -100
    R = 1000
    while L < R:
        midpoint = (L+R)//2
        if midpoint*(midpoint*(midpoint-41)-34)-336 > 0:  # Horner's rule ;)
            R = midpoint
        else:
            L = midpoint + 1
    return L


print(solve())
