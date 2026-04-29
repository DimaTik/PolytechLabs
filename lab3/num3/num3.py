import csv

data = [
	["Имя", "Фамилия", "Оценка"],
	["Анна", "Иванова", 5],
	["Борис", "Петров", 4],
	["Виктор", "Сидоров", 3],
	["Галина", "Кузнецова", 5],
	["Дмитрий", "Соколов", 4]
]

with open("students.csv", "w", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerows(data)

with open("students.csv", "r", encoding="utf-8") as f:
	data = csv.reader(f)
	data = [row for row in data]
	scores = data[1:]
	scores = [float(i[2]) for i in scores]
	print(sum(scores)/len(scores))

with open("students_with_status.csv", "w", encoding="utf-8") as f:
	writer = csv.writer(f)
	data[0].append('Статус')
	for i in range(len(scores)):
		data[i+1] = [*data[i+1], 'Сдал' if scores[i] >= 4 else 'Не сдал']
	writer.writerows(data)
