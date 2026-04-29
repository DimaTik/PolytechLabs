from datetime import date
from typing import List


class Animal:
	def __init__(self, name: str, age: int, breed: str, arrival_date: date):
		self.name = name
		self.age = age
		self.breed = breed
		self.arrival_date = arrival_date
		self.is_adopted = False
		self.medical_history = []

	def add_medical_record(self, record: str) -> None:
		self.medical_history.append(f"{date.today()}: {record}")
		print(f"Добавлена запись для {self.name}: {record}")

	def get_medical_history(self) -> List[str]:
		return self.medical_history

	def get_info(self) -> str:
		status = "доступен" if not self.is_adopted else "усыновлен"
		return f"{self.__class__.__name__}: {self.name}, возраст: {self.age} лет, порода: {self.breed}, статус: {status}"


class Dog(Animal):
	def __init__(self, name: str, age: int, breed: str, arrival_date: date,
	             is_trained: bool = False):
		super().__init__(name, age, breed, arrival_date)
		self.is_trained = is_trained
		self.last_walk_date = None

	def walk(self) -> None:
		self.last_walk_date = date.today()
		print(f"{self.name} выгулян сегодня в парке приюта")

	def train_command(self, command: str) -> None:
		if not self.is_trained:
			self.is_trained = True
		print(f"{self.name} научился команде '{command}'")

	def get_info(self) -> str:
		base_info = super().get_info()
		trained_status = "дрессирована" if self.is_trained else "не дрессирована"
		return f"{base_info}, дрессировка: {trained_status}"


class Cat(Animal):
	def __init__(self, name: str, age: int, breed: str, arrival_date: date,
	             is_vaccinated: bool = False, litter_box_trained: bool = True):
		super().__init__(name, age, breed, arrival_date)
		self.is_vaccinated = is_vaccinated
		self.litter_box_trained = litter_box_trained
		self.toys = []

	def add_toy(self, toy_name: str) -> None:
		self.toys.append(toy_name)
		print(f"Для {self.name} добавлена игрушка: {toy_name}")

	def play(self) -> str:
		if self.toys:
			return f"{self.name} играет с {self.toys[-1]}"
		return f"{self.name} играет с клубком ниток"

	def get_info(self) -> str:
		base_info = super().get_info()
		vax_status = "вакцинирована" if self.is_vaccinated else "не вакцинирована"
		return f"{base_info}, {vax_status}, приучена к лотку: {'да' if self.litter_box_trained else 'нет'}"
