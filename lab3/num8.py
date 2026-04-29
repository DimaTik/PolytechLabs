class TooShortError(Exception):
	"""Пароль должен содержать больше 8 символов"""
	pass

class NoDigitError(Exception):
	"""Пароль должен содержать цифры"""
	pass


def validate_password_with_exception(password):
	if len(password) < 8:
		raise TooShortError("Пароль должен содержать больше 8 символов")
	if [i for i in password if i.isdigit()]:
		raise NoDigitError("Пароль должен содержать цифры")

password = input('Введите пароль для проверки: ')

try:
	validate_password_with_exception(password)
except TooShortError as e:
	print(e)
except NoDigitError as e:
	print(e)