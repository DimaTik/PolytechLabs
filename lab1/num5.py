string = input('Введите строку: ')

res = [i for i in string if i in ('a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')]
print(len(res))
