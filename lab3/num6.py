def find_file(filename):
	try:
		with open(filename, 'r') as f:
			lines = f.readlines()
			print(lines[:10])
	except FileNotFoundError:
		print('Такой файл не найден')
	except PermissionError:
		print('Нет прав на чтение файла')


user_filename = input('Введите название файла: ')
find_file(user_filename)
