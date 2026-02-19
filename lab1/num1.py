hour = int(input("Enter Hour: "))

if hour < 5:
	print("Доброй ночи!")
elif hour < 11:
	print("Доброе утро!")
elif hour < 17:
	print("Добрый день!")
elif hour < 22:
	print("Добрый вечер!")
else:
	print("Доброй ночи!")
