import numpy as np
from os import mkdir
from os.path import isdir
from scikits.odes import ode
from scikits.odes.sundials import CVODESolveFailed, CVODESolveFoundRoot, CVODESolveReachedTSTOP

from DEModelling.initialiser import ode_system
from DEModelling.utils import InitConIndex
from DEModelling.data_format import create_results_file, Solution


def solve_model(*, initial_conditions, solver_config, save_data, folder_name):
    """ Main function which is called by main. We are Solving the Model which we have created.
    """
    # Initialise the time over which to solve the system
    time = np.linspace(solver_config.start, solver_config.stop, int(solver_config.num_time))
    # Calculate the solution to the problem.
    soln, internal_data = calc_numerical_solution(initial_conditions=initial_conditions, solver_config=solver_config,
                                                  time=time)
    internal_data = [0]
    soln_y = soln.values.y
    soln_t = soln.values.t
    soln_flag = [soln.flag]
    jump_times = []

    # Create and save the results file
    if save_data:
        if not isdir(folder_name):
            print("No directory '{}' existed. Creating directory.".format(folder_name))
            try:
                mkdir(folder_name)
            except OSError:
                print("Could not create the directory {}.".format(folder_name))
                print("Fix directory or set save data to False")
                raise SystemExit
            else:
                print("Directory created")

        create_results_file(
            Solution(solution=soln_y, times=soln_t, flags=soln_flag, tstop_times=solver_config.tstop_times,
                     jump_times=jump_times),
            internal_data,
            initial_conditions,
            solver_config,
            folder_name,
        )

    return soln_y, soln_t, soln_flag, internal_data


def calc_numerical_solution(*, initial_conditions, solver_config, time, tstop=0):
    """
    Run the sundials ODE solver on the set of differential equations
    """
    # initialise the differential equation system we want to solve. This is the model we have created
    system_to_solve = ode_system(
        store_internal_data=True
    )

    # Create the sundials system
    solver = ode(
        'cvode',
        system_to_solve,
        old_api=False,
        tstop=tstop,
        validate_flags=True,
        rtol=solver_config.relative_tolerance,
        atol=solver_config.absolute_tolerance,
        max_steps=solver_config.max_steps,
    )

    # and solve it.
    try:
        soln = solver.solve(time, initial_conditions)
    except CVODESolveFailed as e:
        soln = e.soln
        print("Solver: FAILED at time {} with conditions {}".format(soln.values.t[-1], soln.values.y[-1, :]))
    except CVODESolveFoundRoot as e:
        soln = e.soln
        print("Solver: FOUND ROOT at time {} with conditions {}".format(soln.values.t[-1], soln.values.y[-1, :]))
    except CVODESolveReachedTSTOP as e:
        soln = e.soln
        print("Solver: TIME STOP at time {}".format(soln.values.t[-1]))
    # except:  # Bare except for problems with division by zero
    #     raise SystemExit("Something went horribly wrong when trying to solve the ODE. Exiting")

    internal_data = 0

    return soln,  internal_data