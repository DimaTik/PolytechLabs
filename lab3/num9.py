class Garbage(Exception):
	pass

def user_input():
	temp = input("Enter a number: ")
	if temp.isdigit():
		return int(temp)
	else:
		raise Garbage('Вводите пожалуйста только числа')


res = []
while True:
	try:
		temp = user_input()
	except Garbage as e:
		print(e)
	else:
		if temp == 'готово':
			print(sum(res))
			break
		if temp:
			res.append(user_input)
