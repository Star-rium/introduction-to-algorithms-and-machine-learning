import math

def recurrence_exercise1(n):
	'''
	# Solution using caching and looping instead of recursion
	prev = -1
	res = 5
	for i in range(n-1):
		prev = res
		res = prev * 3 - 4
	return res
	'''
	# Solution using recursion
	if n == 1:
		return 5
	prev = recurrence_exercise1(n-1)
	return prev * 3 - 4

def collatz_sequence(n):
	'''
	# Solution using caching and looping instead of recursion
	prev = -1
	res = 25
	for i in range(n-1):
		if res % 2:
			prev = res
			res = prev * 3 + 1
		else:
			prev = res
			res = int(prev / 2)
	return res
	'''
	# Solution using recursion
	if n == 1:
		return 25
	prev = collatz_sequence(n-1)
	return prev * 3 + 1 if prev % 2 else int(prev / 2)

def fibonacci_sequence(n):
	'''
	# Solution using caching and looping instead of recursion
	res = [0, 1]
	for i in range(n-1):
		next_term = res[0] + res[1]
		res[0], res[1] = res[1], next_term

	return res[1]
	'''
	# Solution using recursion (no memoization)
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

def recurrence_exercise4(n):
	'''
	# Solution using caching and looping instead of recursion
	res = [2, -3]
	for i in range(n-1):
		next_term = res[0] * res[1]
		res[0], res[1] = res[1], next_term

	return res[1]
	'''
	# Solution using recursion (no memoization)
	if n <= 0:
		return 2
	if n == 1:
		return -3
	return recurrence_exercise4	(n-1) * recurrence_exercise4(n-2)


if __name__ == '__main__':
	#print(recurrence_exercise1(5))
	#print(collatz_sequence(5))
	#print(fibonacci_sequence(9))
	#print(recurrence_exercise4(5))

