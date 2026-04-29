general_s = ''
with open('part1.txt', 'r') as f:
	general_s += f.read().strip()
with open('part2.txt', 'r') as f:
	general_s += f.read().strip()
print(general_s)
with open('full_text.txt', 'r') as f:
	f.write(general_s)
