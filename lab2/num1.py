def greet(name: str, greeting: str = 'Привет'):
	return f'{greeting}, {name}'

print(greet('Дима'))
