from one_step import solver

def step(f, h, x, y):
	k1 = h * f(x, y)
	k2 = h / 2 * f(x + h / 2, y + k1 / 2)
	k3 = h * f(x + h / 2, y + k2 / 2)
	k4 = h * f(x + h, y + k3)
	return x + h, y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def solution(x0, y0, h, xn, f_ind, eps, c):
	return solver.solution(x0, y0, h, xn, f_ind, eps, c, step, "Рунге-Кутта 4 порядка", 4)