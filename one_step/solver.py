import equations


def solution(x0, y0, h, xn, f_ind, eps, c, step, name, p):
	h1 = h
	yn = None
	y_arr = []
	x_arr = []
	runge = float('inf')
	precise_f = equations.precise[f_ind]
	while True:
		x = x0
		y = y0
		print(f'{name} порядка с шагом {h1}:\n|\tx\t|\ty\t|\ty_p\t|\tdiff\t|')
		if len(y_arr):
			yn = y_arr[-1]
		y_arr = []
		x_arr = []
		while x <= xn:
			print(f'|\t{x:.1f}\t|\t{y:.1f}\t|\t{precise_f(x, y, c):.1f}\t|\t{abs(precise_f(x, y, c) - y):.3f}\t|')
			x_arr.append(x)
			y_arr.append(y)
			x, y = step(equations.derivatives[f_ind], h1, x, y)
		if yn is not None:
			runge = abs(yn - y_arr[-1]) / (2 ** p -1)
		print(f'y^h={yn}, y^h/2={y_arr[-1]}')
		if runge <= eps:
			print('Достигнута нужная точность')
			break
		else:
			print(f'Разница по Рунге равна {runge} > {eps}, пересчитываем')
			h1 /= 2
	return x_arr, y_arr
