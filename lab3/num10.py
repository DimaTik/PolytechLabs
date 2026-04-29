class Book:
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	def describe(self):
		print(f'Название: {self.title}, Автор: {self.author}, Количество страниц: {self.pages}')

book1 = Book('Бойцовский клуб', 'Чак Паланик', 400)
book2 = Book('Укус Питона', 'Swaroop C H', 250)

book1.describe()
book2.describe()