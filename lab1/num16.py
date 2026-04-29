min_number = 0

for i in range(10):
	number = int(input('Введите число: '))
	if number > min_number:
		print(number)
		min_number = number
