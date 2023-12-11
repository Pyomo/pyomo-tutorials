## Write a function that takes in a list of numbers and *prints* the value of the largest number. Be sure to test your function.

def print_max_value(nums):

	print("The max value is: ")
	print(max(nums))


## Write a function that takes a list of numbers and *returns* the largest number

def max_value(nums):

	return max(nums)


## Do so without using any built-in functions

def my_max_value(nums):
	
	tmp = nums[0]
	for i in range(1, len(nums)):
		if nums[i] > tmp:
			tmp = nums[i]

	return tmp

## Call both functions on a couple different lists of numbers to verify they return the same value

l1 = [1, 3, 0, 5, -2]
ans1 = max_value(l1)
print(ans1)
ans2 = my_max_value(l1)
print(ans2)

l2 = [12, 0, 11.9]
print(max_value(l2))
print(my_max_value(l2))


## Write a function that takes a list of numbers and returns a dict consisting of the smallest and largest number 
## (use keys 'smallest' and 'largest'). Be sure to test your function.

def max_and_min(nums):
	
	return {'smallest': min(nums), 'largest': max(nums)}

## Write a function that takes in two lists and prints any common elements between them
## hint: check if an item is in a list using:
## if item in list

def get_common(l1, l2):

	for i in l1:
		if i in l2:
			print(i)


