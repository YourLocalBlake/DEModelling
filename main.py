# Main file currently used for calling models.
import numpy as np
from DEModelling.solver import solve_model
from DEModelling.data_format import ConfigParams, InitialConditions
from DEModelling.utils import ODEIndex


import matplotlib.pyplot as plt

time_start = 0
time_end = 5
time_points = 1000
max_steps = 10000
rel_tor = 1e-4
abs_tor = 1e-6
enable_tstop = 0
tstop_times = [0]
# Only need to specify what ones we require - others will be zero.
initial_x1 = 1
# initial_x1dot = 1  # unused for first order DEs.
# initial_x1ddot = 0
initial_x2 = 2
# initial_x2dot = 0
# initial_x2ddot = 0
initial_x3 = 3
# initial_x3dot = 0
# initial_x3ddot = 0

init_con = InitialConditions(
    init_x1=initial_x1,
    init_x2=initial_x2,
    init_x3=initial_x3
)

solver_config = ConfigParams(
    start=time_start,
    stop=time_end,
    num_time=time_points,
    max_steps=max_steps,
    relative_tolerance=rel_tor,
    absolute_tolerance=abs_tor,
    enable_tstop=enable_tstop,
    tstop_times=tstop_times
)

soln, soln_t, soln_flag, internal_data = solve_model(initial_conditions=init_con, solver_config=solver_config, save_data=False, folder_name="DEModelling_test")

time = np.linspace(time_start, time_end, time_points)
plt.plot(time, soln[:, ODEIndex.x1], label="x1", color='black')
plt.plot(time, soln[:, ODEIndex.x2], label="x2")
plt.plot(time, soln[:, ODEIndex.x3], label="x3", color='red')
plt.legend(loc='best')
plt.show()

# from DEModelling.data_format import solution_loader
# a = solution_loader(file_name="DeModelling_test/TidalStability_2021-01-16--17-11")

