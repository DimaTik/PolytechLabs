weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight/(height**2)

if BMI < 18.5:
	print("Недостаточный вес")
elif BMI < 25:
	print("Норма")
elif BMI < 30:
	print("Избыточный вес")
else:
	print("Ожирение")
