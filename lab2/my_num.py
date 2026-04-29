import random


def positiv(a, b):
	return a>0 and b>0

def random_in_range(a, b):
	return random.randint(a,b)

def deliteli(n):
	res = []
	for i in range(1, n):
		if n % i == 0:
			res.append(i)
	return res

def main():
	a = 0
	b = 0
	while not positiv(a,b):
		a = int(input('Введите первое число: '))
		b = int(input('Введите второе число: '))
	n = random_in_range(a,b)
	print(n)
	print(deliteli(n))


main()
