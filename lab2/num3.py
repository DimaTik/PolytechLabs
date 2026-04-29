def celsius_to_fahrenheit(celsius):
	return (celsius * (9/5)) + 32

def fahrenheit_to_celsius(f):
	return (f - 32) * 5/9

def main():
	def_type = input("Выберите изначальное значение c/f ")
	if def_type == "c":
		degree = int(input("Введите градусы: "))
		print(celsius_to_fahrenheit(degree))
	else:
		degree = int(input("Введите градусы: "))
		print(fahrenheit_to_celsius(degree))

main()
