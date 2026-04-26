import math

def binary_to_decimal(string):
	res = 0
	for i in range(len(string)):
		if string[i] == "1":
			res += 2**(len(string)-(i+1))
	return res

def hexadecimal_to_decimal(string):
	# map the letter characters in the hex base
	letter_map = {
		"a": 10,
		"b": 11,
		"c": 12,
		"d": 13,
		"e": 14,
		"f": 15
	}
	res = 0
	for i in range(len(string)):
		if string[i].lower() in letter_map:
			res += letter_map[string[i].lower()]*16**(len(string)-(i+1))
		else:
			res += int(string[i])*16**(len(string)-(i+1))
	return res

def decimal_to_binary(num):
	if num == 0: # Edge case 0
		return "0"

	res = ""
	while num > 0:
		res += str(num%2)
		num = num//2

	return res[::-1] 

def decimal_to_hexadecimal(num):
	if num == 0: # Edge case 0
		return "0"
		
	letter_map = {
		10: "a",
		11: "b",
		12: "c",
		13: "d",
		14: "e",
		15: "f"
	}
	res = ""
	while num > 0:
		res += str(num%16) if num%16 < 10 else letter_map[num%16]
		num = num//16
	return res[::-1]

def binary_to_hexadecimal(string):
	decimal_num = binary_to_decimal(string)
	hex_res = decimal_to_hexadecimal(decimal_num)
	return hex_res

def hexadecimal_to_binary(string):
	decimal_num = hexadecimal_to_decimal(string)
	binary_res = decimal_to_binary(decimal_num)
	return binary_res

if __name__ == '__main__':
	#print(binary_to_decimal("11010"))
	#print(hexadecimal_to_decimal("3B07F"))
	#print(decimal_to_binary(26))
	#print(decimal_to_hexadecimal(241791))

	pass
