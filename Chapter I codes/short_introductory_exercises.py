def check_if_symmetric(string):
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
	return "".join(chr(num + 96) if num != 0 else " " for num in arr) # assuming the number ranges from 0-26

if __name__ == '__main__':
	# print(check_if_symmetric("aabb"))
	# print(convert_to_numbers("a cat"))
	# print(convert_to_letters([1, 0, 2, 3]))
	pass