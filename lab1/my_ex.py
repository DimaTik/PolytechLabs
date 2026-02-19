"""
13.	Вводить строку до тех пор, пока не выполнятся условия:
Сумма цифр в строке не превышает максимальную цифру более чем на 3.
"""

string = ''
while True:
	string += input("Введите число: ")
	if sum(map(int, list(string))) - max(map(int, list(string))) > 3:
		break
	else:
		print(string)
print(string)

