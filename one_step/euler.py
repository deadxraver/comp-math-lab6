from one_step import solver


def step(f, h, x, y):
	return x + h, y + h * f(x, y)


def solution(x0, y0, h, xn, f_ind, eps, c):
	return solver.solution(x0, y0, h, xn, f_ind, eps, c, step, "Эйлера", 1)
