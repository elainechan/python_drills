'''
rangoli.py

Design a function that prints an alphabet rangoli of size n.
Input: An integer n where: 0 < n < 27
Output: Print the alphabet rangoli.
The center of the rangoli has the first alphabet letter a, 
The boundary has the last alphabet letter indicated.
'''


import string

def rangoli(n):
	
    alpha = list(string.ascii_lowercase)  # Last letter is alphabet[n - 1]

# Map n to number of dashes on each side of first row

    side_dashes = dict(list({0:0, 1:0}.items()) + list(dict(zip(range(2, 27), range(2, 52, 2))).items()))
    k = side_dashes.keys()
    v = side_dashes.values()

# List elements, each of length 27 including when n = 0:

    letters = [0, 1] + list(range(2, 27))  # Number of letters
    dash_len = [0, 0] + list(range(2, 52, 2))  # Number of dashes in first row
    row_num = [0] + list(range(1, 53, 2))  # Number of rows = n * 2 - 1
    row_len = [0, 1, 5, 9, 13, 17]  

# Print rows until all letters have been used, then reverse print pattern

# Padding on each side of letter string: pad = '-'
# Separator between letters: delimiter = '-'

    print(side_dashes)
    print(dash_len)
    print(row_len)

# Rules:
# 1) Number of rows = n * 2 - 1
# 2) row_len = 
# 3) Start in descending order
# 4) Always print a dash between two letters
# 5) Always use the last letter as boundary
# 6) Row numbers are always odd except for 0

# Example: let n = 3
# 1  ----c----  Row length = 9
# 2  --c-b-c--  
# 3  c-b-a-b-c
# 4  --c-b-c--  Repeats Row 2
# 5  ----c----  Repeats Row 1

# Note: on each row, if the position index is even, there is a dash.

# Pseudocode for manual n = 3 example:
# Row 1: print v dashes, 'c', v dashes
#	print('-' * v + alphabet[n - 1] + '-' * v)
# Row 2: print v - 2 dashes, 'c', dash, 'b', dash, 'c', v - 2 dashes
#	print('-' * (v - 2), alphabet[n - 1], '-', alphabet[n - 2], ...)
# Row 3: print c dash b dash a dash b dash c
# Row 4 = Row 2
# Row 5 = Row 1
