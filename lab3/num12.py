from typing import List


class MenuItem:
	def __init__(self, name: str, price: float):
		self.name = name
		self.price = price


class Order:
	def __init__(self, items: List[MenuItem]):
		self.items = items

	def add_item(self, item: MenuItem):
		self.items.append(item)

	def calculate_total(self):
		return sum([i.price for i in self.items])

	def print_receipt(self):
		string = ''
		for i in self.items:
			string += f'{i.name}: {str(i.price)}\n'
		return string + f'Итого: {self.calculate_total()}'
