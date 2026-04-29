def find_keyword(**kwargs):
	for k, v in kwargs.items():
		if isinstance(v, str) and v.lower() == 'секрет':
			print(k)

find_keyword(name="Анна", code="Секрет", id=10)
