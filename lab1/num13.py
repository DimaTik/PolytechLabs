number = input('Введите число: ')

string = [f'{i}+' for i in number]
print(f"{''.join(string)[:-1]}={sum(map(int, list(number)))}")
