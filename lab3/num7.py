def robust_convert_to_int(string):
	try:
		return int(string)
	except ValueError:
		return None

print(robust_convert_to_int('123sd'))
