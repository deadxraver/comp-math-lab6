import equations
import graph
import one_step.euler

# Это будет вводиться с клавиатуры
f_ind = 1
x0 = 0
xn = 0.2
y0 = 1
h = 0.1
eps = 0.01

# Это будем использовать
precise_f = equations.precise[f_ind]
c = y0 - precise_f(x0, 0)

graph.create_plot()
graph.add_function(lambda x: precise_f(x, c), [x0, xn], label='Точное', color='red')
euler_x_arr, euler_y_arr = one_step.euler.solution(x0, y0, h, xn, f_ind, eps, c)



graph.add_points(euler_x_arr, euler_y_arr, color='black', label='Эйлер')
graph.show()
