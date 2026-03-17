def check_brackets(text):
	if len(text) % 2 != 0:
		print('Неправильно расставлены скобки')
		return
	copy_text = text
	for i, j in zip(('(', '[', '{', ')', ']', '}'), (0, 1, 2, 0, 1, 2)):
		copy_text = copy_text.replace(i, str(j))
	first_part = copy_text[:len(text)//2]
	second_part = copy_text[len(text)//2:][::-1]
	if first_part == second_part:
		print('Скобки правильные')
	else:
		print('Скобки неправильные')

check_brackets('({})')
