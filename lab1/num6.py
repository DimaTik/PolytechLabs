from random import randint

number = randint(1, 11)
print(number)

cnt = 1
while pred_number := int(input("Enter a number: ")) != number:
	if pred_number > number:
		print('Меньше')
	else:
		print('Больше')
	cnt += 1
print(f'Вы угадали число! Количество попыток = {cnt}')
