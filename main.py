import equations
import graph
import one_step.euler

euler_x_arr = []
euler_y_arr = []
f_ind = 1
x = 0
xn = 6
y = 1
h = 0.1
eps = 0.001
c = y - equations.precise[f_ind](x, 0)
graph.create_plot()
graph.add_function(lambda x: equations.precise[f_ind](x, c), [x, xn], label='Точное', color='red')
while x < xn:
	euler_x_arr.append(x)
	euler_y_arr.append(y)
	x, y = one_step.euler.step(equations.derivatives[f_ind], h, x, y)

graph.add_points(euler_x_arr, euler_y_arr, color='black', label='Эйлер')
graph.show()
