import math

def square_area(a: float):
	return a*a

def rectangle_area(a: float, b: float):
	return a*b

def circle_area(r: float):
	return math.pi*r*r

print(square_area(4))
print(rectangle_area(4, 5))
print(circle_area(6))
