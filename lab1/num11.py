number = int(input("Enter a number: "))

arr = [f'{number}*{i}={number*i}' for i in range(1, 11)]
for i in arr:
	print(i)
