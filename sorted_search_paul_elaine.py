'''
sorted_search.py
Input:
You have an element x, and a list named listy. 
The list contains sorted, positive integers. 
Find the index at which an element x occurs in listy. 
If x occurs multiple times, you may return any of those indices.

Output:
Return a single integer that represents the index 
at which the input element x occurs in the input listy.
If element x is not in listy, return -1.
'''

def find(x, listy):
	
	min_index = 0
	max_index = len(listy)

	if listy == []:
			return -1

	while min_index < max_index:

		pointer = (max_index + min_index)//2
		
		if listy[pointer] == x:  # Bingo! x is right at the pointer
			return pointer
		
		elif abs(max_index - min_index) <= 1:  # We've run out of list and x != pointer
			return -1
		
		elif listy[pointer] > x:  # The pointer is to the right of x
			max_index = pointer
		
		elif listy[pointer] < x:  # The pointer is to the left of x
			min_index = pointer

	return -1


def find(target, listy):

	size = len(listy)
	lo = 0
	hi = size - 1

	while lo <= hi:
		
		mid = (hi + lo) // 2

		if target == listy[mid]:
			return mid

		elif target < listy[mid]:
			hi = mid - 1

		else:
			lo = mid + 1

	return 1

def find(x,listy):

	first=0
	last=len(listy)-1

	while first <= last:

		mid = (first+last)//2

		if listy[mid] == x:
			return mid
		
		if x < listy[mid]:
			last = mid - 1
		
		else:
			first = mid + 1
	return -1