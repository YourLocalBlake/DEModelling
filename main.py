# Main file currently used for calling models.

from DEModelling.solver import calc_numerical_solution
from numpy import linspace

import matplotlib.pyplot as plt

time_start = 0
time_end = 20
num_points = 1000
initial_x = 0
inital_xdot = 1
initial_conditions = [initial_x, inital_xdot]


sol = calc_numerical_solution(initial_conditions=initial_conditions, time=time_start, tstop=time_end)

y_points = [i[0] for i in sol.values.y]
ydot_point = [i[1] for i in sol.values.y]

plt.plot(linspace(time_start, time_end, num_points), y_points)
plt.show()
