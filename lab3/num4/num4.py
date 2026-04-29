def replace_in_file(filename, old_word, new_word):
	with open(filename, 'r') as f:
		s = f.read()
	s = s.replace(old_word, new_word)
	with open(filename, 'w') as f:
		f.write(s)

replace_in_file('record.txt', 'old', 'elephant')
