import numpy as np
from scikits.odes import ode
from scikits.odes.sundials import CVODESolveFailed, CVODESolveFoundRoot, CVODESolveReachedTSTOP

from DEModelling.initialiser import ode_system_1_var
from DEModelling.utils import InitConIndex


def calc_numerical_solution(*, initial_conditions, time, tstop):
    """
    Run the sundials ODE solver on the set of differential equations
    """

    # initialise the differential equation model
    system = ode_system_1_var(
        x=initial_conditions[InitConIndex.x],
    )

    # Create the sundials system
    solver = ode(
        'cvode', system,
        old_api=False,
        tstop=tstop,
    )
    time = np.linspace(time, tstop, int(1000))
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

    return soln