import string

def validate_password(password):
	validate_dict = {
		"length_ok": False,
		"has_digit": False,
		"has_upper": False,
		"is_valid": False
	}
	if len(password) >= 8:
		validate_dict["length_ok"] = True
	if [i for i in password if i.isdigit()]:
		validate_dict["has_digit"] = True
	if [i for i in password if i in string.ascii_uppercase]:
		validate_dict["has_upper"] = True
	if all([validate_dict["length_ok"], validate_dict["has_digit"], validate_dict["has_upper"]]):
		validate_dict["is_valid"] = True
	return validate_dict


def main():
	password = input("Enter your password: ")
	print(validate_password(password))
