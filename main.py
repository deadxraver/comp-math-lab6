import equations
import graph
import one_step.euler
import one_step.rk4
import multi_step.miln

# Это будет вводиться с клавиатуры
f_ind = 1
x0 = 0
xn = 2
y0 = 1
h = 0.1
eps = 0.01

# Это будем использовать
precise_f = equations.precise[f_ind]
c = y0 - precise_f(x0, y0, 0)

graph.create_plot()
graph.add_function(lambda x: precise_f(x, 0, c), [x0, xn], label=f'Точное, {equations.text_precise[f_ind]}', color='black')

euler_x_arr, euler_y_arr = one_step.euler.solution(x0, y0, h, xn, f_ind, eps, c)
rk4_x_arr, rk4_y_arr = one_step.rk4.solution(x0, y0, h, xn, f_ind, eps, c)
miln_x_arr, miln_y_arr = multi_step.miln.solution(x0, y0, h, xn, f_ind, eps, c)

graph.add_points(euler_x_arr, euler_y_arr, color='red', label='Эйлер')
graph.add_points(rk4_x_arr, rk4_y_arr, color='green', label='Рунге-Кутта 4 порядка')
if miln_x_arr is not None: graph.add_points(miln_x_arr, miln_y_arr, color='blue', label='Милн')
graph.show()
