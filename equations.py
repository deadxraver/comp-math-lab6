import math

derivatives = [
	lambda x, y: x ** 2 + 2,
	lambda x, y: math.sin(x),
	lambda x, y: 1,
]

precise = [
	lambda x, y, c: x ** 3 / 3 + 2 * x + c,
	lambda x, y, c: -math.cos(x) + c,
	lambda x, y, c: x + c,
]

text_der = [
	"f'(x, y) = x^2 + 2",
	"f'(x, y) = sinx",
	"f'(x, y) = 1",
]

text_precise = [
	"f(x, y) = x^3 / 3 + 2 * x + C",
	"f(x, y) = -cosx + C",
	"f(x, y) = x + C",
]
