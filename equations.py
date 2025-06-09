import math

derivatives = [
	lambda x: x**2 + 2,
	lambda x: math.sin(x),
]

precise = [
	lambda x, c: x**3 / 3 + 2 * x + c,
	lambda x, c: -math.cos(x) + c
]