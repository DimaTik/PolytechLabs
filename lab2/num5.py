def calculate(operation: str, a, b):
	try:
		res = eval(f"{a}{operation}{b}")
	except ZeroDivisionError:
		print('Нельзя делить на ноль')


operation = input('Введите операцию: ')
a = float(input('Введите первое значение: '))
b = float(input('Введите второе значение: '))
print(calculate(operation, a, b))
