import math

def check_if_symmetric(string):
	# basic palindrome problem, check the head and the tail till meet the middle
	for i in range(int(len(string)/2)):
		if string[i] != string[len(string)-i-1]:
			return False
	return True

def convert_to_numbers(string):
	'''
	Solution without list comprehension

	result = []
	for letter in string:
		if letter == " ":
			result.append(0)
		else:
			result.append(ord(letter.lower()) - 96) # assuming the string only consist of lower case characters
	return result
	'''
	return [ord(letter) - 96 if letter != " " else 0 for letter in string]

def convert_to_letters(arr):
	# solution without list comprehension should be similar to the last one
	return "".join(chr(num + 96) if num != 0 else " " for num in arr) # assuming the number ranges from 0-26

def get_intersection(array1, array2):
	# considering both array can have multiple types of values, no duplicates, and can have different length
	# naive solution: looping through 1 array to check similarities
	# expected time complexity: O(n+m)

	result = []
	i = 0
	set2 = [(type(x), x) for x in array2] # Create another array (since set is banned) for storing both the type and value of each value in array2
	# This is because the boolean value True and 1 are considered the same, so we have to compare types as well
	for item in array1:
		if (type(item), item) in set2:
			if item not in result:
				result.append(item)
	return result

def get_union(array1, array2):
	# similar to intersection and not allowed to use set()
	# expected time complexity: O(n)
	seen = {}

	for value in array1 + array2:
		# using dict to list seen values as dict keys must be unique
		key = (type(value), value)
		if key not in seen:
			seen[key] = value

	return list(seen.values())

def count_characters(string):
	result = {}
	for letter in string:
		lowered_letter = letter.lower()
		if lowered_letter not in result:
			result[lowered_letter] = 1 # initialize key in the hash map
		else:
			result[letter.lower()] += 1 # add 1 to the hash map for every encounter
	return result

def is_prime(N):
	# pretty self-explanatory, unless you want to do some instant calculation i suggest looking up Gandhi's Formula
	if N < 2: return False
	for i in range(2, math.floor(N/2)):
		if N%i == 0:
			return False
	return True

if __name__ == '__main__':
	# print(check_if_symmetric("aabb"))
	# print(convert_to_numbers("a cat"))
	# print(convert_to_letters([1, 0, 2, 3]))
	# print(get_intersection(['a', 1, True, 'baba', 'c'], [1, 'dadw', False, 'a', 'bcacba', 8.23]))
	# print(get_union(['a', 1, True, 'baba', 'c'], [1, 'dadw', False, 'a', 'bcacba', 8.23]))
	# print(count_characters("A cat!!!"))
	# print(is_prime(2))
	pass