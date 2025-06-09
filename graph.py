import numpy as np
import matplotlib.pyplot as plt


def create_plot(figsize=(10, 6)):
	plt.figure(figsize=figsize)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True, alpha=0.3)


def add_function(func, interval, label=None, color=None):
	if func is None:
		return
	linestyle = '-'
	a, b = interval
	x = np.linspace(a, b, 500)
	y = np.vectorize(func)(x)

	plt.plot(x, y,
			 label=label,
			 color=color,
			 linestyle=linestyle,
			 zorder=1)


def add_points(x_arr, y_arr, label=None, color='red'):
	marker_size = 300 / len(x_arr)
	if marker_size > 10:
		marker_size = 10
	x_points = np.array(x_arr)
	y_points = np.array(y_arr)
	plt.plot(x_points, y_points,
			 color=color,
			 marker='o',
			 markersize=marker_size,
			 zorder=2,
			 label=label,
			 markerfacecolor=color,
			 markeredgecolor='black')


def show():
	plt.title('Графики решений')
	plt.legend()
	plt.show()
