count = 0

def counter(func):
	def wrapper():
		global count
		count += 1
		func()
	return wrapper


@counter
def main():
	print('Привет, я отработал, иду спать')

for i in range(11):
	main()

print(count)