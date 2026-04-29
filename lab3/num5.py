def calculate(operation: str, a, b):
	try:
		return eval(f"{a}{operation}{b}")
	except ZeroDivisionError:
		print('Нельзя делить на ноль')
	except ValueError:
		print('Программа требует числа на вводе')


while True:
	operation = input('Введите операцию: ')
	a = float(input('Введите первое значение: '))
	b = float(input('Введите второе значение: '))
	res = calculate(operation, a, b)
	if res:
		break