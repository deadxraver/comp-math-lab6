import equations
import one_step.rk4


def solution(x0, y0, h, xn, f_ind, eps, c):
	x_arr = [x0]
	y_arr = [y0]
	f = equations.derivatives[f_ind]
	f_arr = [f(x0, y0)]
	precise_f = equations.precise[f_ind]
	print(f'Первые 3 точки с помощью Рунге-Кутта 4 порядка с шагом {h}:\n|\tx\t\t|\ty\t\t|\ty_p\t\t|\tdiff\t|')
	for i in range(3):
		x, y = one_step.rk4.step(equations.derivatives[f_ind], h, x_arr[-1], y_arr[-1])
		print(f'|\t{x:.3f}\t|\t{y:.3f}\t|\t{precise_f(x, y, c):.3f}\t|\t{abs(precise_f(x, y, c) - y):.3f}\t|')
		x_arr.append(x)
		y_arr.append(y)
		f_arr.append(f(x, y))

	if x_arr[-1] > xn:
		print("Слишком короткий промежуток или слишком большой шаг, вышли за предел при вычислении первых трех точек!")
		return None, None
	print(f'Милн с шагом {h}:\n|\tx\t\t|\ty\t\t|\ty_p\t\t|\tdiff\t|')
	y_pred = None
	while x_arr[-1] <= xn:
		if y_pred is None:
			print(
				f'|\t{x_arr[-1]:.3f}\t|\t{y_arr[-1]:.3f}\t|\t{precise_f(x_arr[-1], y_arr[-1], c):.3f}\t|\t{abs(precise_f(x_arr[-1], y_arr[-1], c) - y_arr[-1]):.3f}\t|')
			y_pred = y_arr[-4] + 4 * h / 3 * (2 * f_arr[-3] - f_arr[-2] + 2 * f_arr[-1])
		f_pred = f(x_arr[-1] + h, y_pred)
		y_corr = y_arr[-2] + h / 3 * (f_arr[-2] + 4 * f_arr[-1] + f_pred)
		if abs(y_corr - y_pred) > eps:
			y_pred = y_corr
		else:
			y_pred = None
			diff = abs(y_arr[-1] - precise_f(x_arr[-1], y_arr[-1], c))
			y_arr.append(y_corr)
			x_arr.append(x_arr[-1] + h)
			f_arr.append(f(x_arr[-1], y_arr[-1]))
			if diff > eps:
				print(f'Вышли за допустимую точность ({diff} > {eps}), пересчитаем с меньшим шагом')
				return solution(x0, y0, h / 2, xn, f_ind, eps, c)
	return x_arr, y_arr
