import equations
import one_step.rk4


def solution(x0, y0, h, xn, f_ind, eps, c):
	x_arr = [x0]
	y_arr = [y0]
	f = equations.derivatives[f_ind]
	f_arr = [f(x0, y0)]
	for i in range(3):
		x, y = one_step.rk4.step(equations.derivatives[f_ind], h, x_arr[-1], y_arr[-1])
		x_arr.append(x)
		y_arr.append(y)
		f_arr.append(f(x, y))
	if x_arr[-1] > xn:
		print("Слишком короткий промежуток или слишком большой шаг, вышли за предел при вычислении первых трех точек!")
		return None, None
	while x_arr[-1] <= xn:
		y_pred = y_arr[-4] + 4 * h / 3 * (2 * f_arr[-3] - f_arr[-2] + 2 * f_arr[-1])
		x_arr.append(x_arr[-1] + h)
		f_pred = f(x_arr[-1], y_pred)
		f_arr.append(f_pred)
		y_arr.append(y_arr[-2] + h / 3 * (f_arr[-2] + 4 * f_arr[-1] + f_pred))
		diff = abs(y_arr[-1] - equations.precise[f_ind](x_arr[-1], y_arr[-1], c))
		if diff > eps:
			print(f'Вышли за допустимую точность ({diff} > {eps}), пересчитаем с меньшим шагом')
			return solution(x0, y0, h / 2, xn, f_ind, eps, c)
	return x_arr, y_arr