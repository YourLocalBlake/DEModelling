# Main file currently used for calling models.

from DEModelling.solver import calc_numerical_solution
from numpy import linspace

import matplotlib.pyplot as plt

time_start = 0
time_end = 5
num_points = 1000
initial_x = 1
initial_xdot = 1  # unused for first order DEs.
initial_conditions = [initial_x, initial_xdot]

models = ["x", "x2", "x3", "const_1", "const_2", "2x"]


sol = calc_numerical_solution(model=models[0], initial_conditions=initial_conditions, time=time_start, tstop=time_end)

y_points = [i[0] for i in sol.values.y]
ydot_points = [i[1] for i in sol.values.y]

plt.plot(linspace(time_start, time_end, num_points), y_points, color='red')
plt.plot(linspace(time_start, time_end, num_points), ydot_points, color='green')
plt.show()
