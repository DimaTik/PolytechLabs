number = int(input("Enter a number: "))

if number % 2 == 0:
	print('Число четное')
else:
	print('Число нечетное')

if number % 5 == 0:
	print('Число делится на 5')
else:
	print('Число не делится на 5')

if number % 3 == 0 and number % 2 == 0:
	print('Число делится на 2 и на 3')
else:
	print('Число не делится на 2 и на 3')
