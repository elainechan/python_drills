"""
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input:
The first line contains an integer, N (the size of our array). 
The second line contains N space-separated integers describing array A's elements.

Output:
Print the elements of array A in reverse order as a single line of space-separated numbers.
"""
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(arr)
arr1 = list(reversed(arr))
arr2 = list(map(str, arr1))
            
print(arr1)
print(arr2)
print(" ".join(x for x in arr2))