from short_introductory_exercises import check_if_symmetric, convert_to_numbers, convert_to_letters, get_intersection, get_union, count_characters, is_prime

# All test cases goes here
# Note to whoever cloned this repo from my github: I highly encourage you to change or add more test cases, dig deeper to each of them as i can miss some snitchy edge cases here.
tests = [
	# Palindrome section
	{
		'function': check_if_symmetric,
		'input': 'level',
		'output': True
	},
	{
		'function': check_if_symmetric,
		'input': 'A man, a plan, a canal: Panama',
		'output': False
	},
	{
		'function': check_if_symmetric,
		'input': 'a',
		'output': True
	},
	{
		'function': check_if_symmetric,
		'input': '',
		'output': True
	},
	{
		'function': check_if_symmetric,
		'input': 'abba',
		'output': True
	},
	# String to numbers section
	{
		'function': convert_to_numbers,
		'input': "a cat",
		'output': [1, 0, 3, 1, 20]
	},
	{
		'function': convert_to_numbers,
		'input': "abcd",
		'output': [1, 2, 3, 4]
	},
	{
		'function': convert_to_numbers,
		'input': "xyz",
		'output': [24, 25, 26]
	},
	{
		'function': convert_to_numbers,
		'input': "a cat",
		'output': [1, 0, 3, 1, 20]
	},
	{
		'function': convert_to_numbers,
		'input': "aaa",
		'output': [1, 1, 1]
	},
	{
		'function': convert_to_numbers,
		'input': "",
		'output': []
	},
	# Numbers to string section
	{
		'function': convert_to_letters,
		'input': [1, 2, 3],
		'output': "abc"
	},
	{
		'function': convert_to_letters,
		'input': [1, 0, 2],
		'output': "a b"
	},
	{
		'function': convert_to_letters,
		'input': [24, 25, 26, 0],
		'output': "xyz "
	},
	{
		'function': convert_to_letters,
		'input': [],
		'output': ""
	},
	{
		'function': convert_to_letters,
		'input': [8, 5, 12, 12, 15],
		'output': "hello"
	},
	# Intersection problem section
	{
		'function': get_intersection,
		'input': [[1, 2, "a"],[2, "a", 3]],
		'output': [2, "a"]
	},
	{
		'function': get_intersection,
		'input': [[1, 2, 3], ["x", "y"]],
		'output': []
	},
	{
		'function': get_intersection,
		'input': [[1], [1, 2, 3, 4, 5]],
		'output': [1]
	},
	{
		'function': get_intersection,
		'input': [[1, 1, 2], [1, 2, 2]],
		'output': [1, 2]
	},
	{
		'function': get_intersection,
		'input': [[], [1, 2]],
		'output': []
	},
	{
		'function': get_intersection,
		'input': [["1", 2], [1, "2"]],
		'output': []
	},
	{
		'function': get_intersection,
		'input': [[1.0, 2.5], [1, 3.0]],
		'output': [1.0] # note to self: return to this edge case later.
	},
	{
		'function': get_intersection,
		'input': [['a', 1, True, 'baba', 'c'], [1, 'dadw', False, 'a', 'bcacba', 8.23]],
		'output': ['a', 1]
	},
	# Union problem section:
	{
		'function': get_union,
		'input': [[1, 2, 'a'], [2, 'a', 3]],
		'output': [1, 2, 'a', 3]
	},
	{
		'function': get_union,
		'input': [[1, True, 0], [False, 1, 2]],
		'output': [1, True, 0, False, 2]
	},
	{
		'function': get_union,
		'input': [[1.0, 2], [1, 3.0]],
		'output': [1.0, 2, 1, 3.0]
	},
	{
		'function': get_union,
		'input': [['x', 'y'], [1, 2]],
		'output': ['x', 'y', 1, 2]
	},
	{
		'function': get_union,
		'input': [[], [1, 2, 3]],
		'output': [1, 2, 3]
	},
	{
		'function': get_union,
		'input': [[1, 1, 2], [2, 3, 3]],
		'output': [1, 2, 3]
	},
	{
		'function': get_union,
		'input': [[1], [1, 2, 3, 4, 5]],
		'output': [1, 2, 3, 4, 5]
	},
	{
		'function': get_union,
		'input': [['1', 2, None], [1, '2', None]],
		'output': ['1', 2, None, 1, '2']
	},
	# Count characters sections
	{
		'function': count_characters,
		'input': "hello",
		'output': {'h': 1, 'e': 1, 'l': 2, 'o': 1}
	},
	{
		'function': count_characters,
		'input': "aaaaa",
		'output': {'a': 5}
	},
	{
		'function': count_characters,
		'input': "",
		'output': {}
	},
	{
		'function': count_characters,
		'input': "a A a!",
		'output': {'a': 3, ' ': 2, '!': 1}
	},
	{
		'function': count_characters,
		'input': "123123",
		'output': {'1': 2, '2': 2, '3': 2}
	},
	{
		'function': count_characters,
		'input': "x",
		'output': {'x': 1}
	},
	{
		'function': count_characters,
		'input': "\n\t ",
		'output': {'\n': 1, '\t': 1, ' ': 1}
	},
	{
		'function': count_characters,
		'input': "racecar",
		'output': {'r': 2, 'a': 2, 'c': 2, 'e': 1}
	},
	# Is prime? Section
	{
		'function': is_prime,
		'input': 7,
		'output': True
	},
	{
		'function': is_prime,
		'input': 2,
		'output': True 
	},
	{
		'function': is_prime,
		'input': 1,
		'output': False
	},
	{
		'function': is_prime,
		'input': 0,
		'output': False
	},
	{
		'function': is_prime,
		'input': -7,
		'output': False
	},
	{
		'function': is_prime,
		'input': 9,
		'output': False
	},
	{
		'function': is_prime,
		'input': 97,
		'output': True
	},
	{
		'function': is_prime,
		'input': 77,
		'output': False
	}

]

num_successes = 0
num_failures = 0

for test in tests:
	function = test['function']
	test_input = test['input']
	desired_output = test['output']
	if function.__name__ == "get_intersection" or function.__name__ == "get_union":
		actual_output = function(test_input[0], test_input[1])
	else:
		actual_output = function(test_input)

	if actual_output == desired_output:
		num_successes += 1
	else:
		num_failures += 1
		function_name = function.__name__
		print(f"\n{function_name} failed on input: {test_input}\nActual output: {actual_output}\nDesired output: {desired_output}")

print(f"Testing complete: {num_successes} successes and {num_failures} failures")