# Main file currently used for calling models.
import numpy as np
from DEModelling.solver import solve_model
from DEModelling.data_format import ConfigParams
from DEModelling.utils import ODEIndex


import matplotlib.pyplot as plt

time_start = 0
time_end = 5
time_points = 1000
initial_x1 = 1
initial_x1dot = 1  # unused for first order DEs.
initial_x1ddot = 0
initial_x2 = 2
initial_x2dot = 0
initial_x2ddot = 0
initial_x3 = 3
initial_x3dot = 0
initial_x3ddot = 0
initial_conditions = [initial_x1, initial_x1dot, initial_x1ddot, initial_x2, initial_x2dot, initial_x2ddot, initial_x3, initial_x3dot, initial_x3ddot]

solver_config = ConfigParams(
    start=time_start,
    stop=time_end,
    num_time=time_points,
    max_steps = 10000,
    relative_tolerance = 1e-4,
    absolute_tolerance = 1e-4,
    enable_tstop = 0,
    tstop_times = [0]
)


soln, soln_t, soln_flag, internal_data = solve_model(initial_conditions=initial_conditions, solver_config=solver_config, save_data=False, folder_name="DEModelling_test")

# y_points = [i[0] for i in sol.values.y]
# ydot_points = [i[1] for i in sol.values.y]
#
# plt.plot(linspace(time_start, time_end, time_points), y_points, color='red')
# plt.plot(linspace(time_start, time_end, time_points), ydot_points, color='green')
# plt.show()
time = np.linspace(time_start, time_end, time_points)
plt.plot(time, soln[:, ODEIndex.x1], label="x1", color='black')
plt.plot(time, soln[:, ODEIndex.x2], label="x2")
plt.plot(time, soln[:, ODEIndex.x3], label="x3", color='red')
plt.legend(loc='best')
plt.show()
