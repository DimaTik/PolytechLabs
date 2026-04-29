class BankAccount:
	def __init__(self, owner, balance):
		self.owner = owner
		self.__balance = balance

	def deposit(self, amount):
		self.__balance += amount
		print(f'Вы успешно пополнили баланс на {amount}. Баланс после операции {self.__balance}')

	def withdraw(self, amount):
		if amount < self.__balance:
			self.__balance -= amount
			print(f'Вы успешно сняли средства с баланса на сумму {amount}. Баланс после операции {self.__balance}')

	def get_balance(self):
		return self.__balance
