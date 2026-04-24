from short_introductory_exercises import check_if_symmetric
from short_introductory_exercises import convert_to_numbers

# All test cases goes here
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
]

num_successes = 0
num_failures = 0

for test in tests:
	function = test['function']
	test_input = test['input']
	desired_output = test['output']
	actual_output = function(test_input)

	if actual_output == desired_output:
		num_successes += 1
	else:
		num_failures += 1
		function_name = function.__name__
		print(f"\n{function_name} failed on input: {test_input}\nActual output: {actual_output}\nDesired output: {desired_output}")

print(f"Testing complete: {num_successes} successes and {num_failures} failures")