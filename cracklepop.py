# Write a program that prints out the numbers 1 to 100 (inclusive). 
integers_list = list(range(1, 101))

# Test to see you have the right list of numbers.
print(integers_list)

for i in integers_list:
	# If it's divisible by both 3 and 5, print CracklePop instead of the number.
	if i % 3 == 0 and i % 5 == 0:
		print("CracklePop", end = ' ')
	# If it's divisible by 5, print Pop instead of the number.
	elif i % 5 == 0: 
		print("Pop", end = ' ')
	# If the number is divisible by 3, print Crackle instead of the number. 
	elif i % 3 == 0:
		print("Crackle", end = ' ')
	# Otherwise, print the number.
	else: 
		print(i, end = ' ')