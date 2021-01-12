# Contains the functions to solve the model given from models.py

from DEModelling.models.one_var import *
from DEModelling.utils import ODEIndex


def ode_system(*, store_internal_data=True):
    """
        Create the mathematical ODE model.
        Returns the sundials ode model which will be solved.
    """

    # The internal data allows the user to obtain the solved values of any variable they want at each time step.
    # if store_internal_data:
    #     internal_data = InternalData()
    #     times_list = internal_data.times
    #     params_list = internal_data.params
    #     derivs_list = internal_data.derivs
    #     a1_list = internal_data.a1
    #     a2_list = internal_data.a2
    #     a3_list = internal_data.a3
    #     a1dot_list = internal_data.a1dot
    #     a2dot_list = internal_data.a2dot
    #     a3dot_list = internal_data.a3dot
    #     problems = internal_data.problems
    # else:
    #     internal_data = None

    def rhs_equation(time, params, derivs):
        """
        RHS of the ODE equations
        Inputs are passed by Sundials.
        """
        # Specify the variables of the system.
        x = params[ODEIndex.x]
        y = params[ODEIndex.y]
        z = params[ODEIndex.z]
        θ = params[ODEIndex.θ]
        ϕ = params[ODEIndex.ϕ]
        xdot = params[ODEIndex.xdot]
        ydot = params[ODEIndex.ydot]
        zdot = params[ODEIndex.zdot]

        # First order derivative functions
        # Place here the RHS of the equation.
        # i.e. x' = 2x + 3 would be deriv_x = model_2x_plus_3_func()
        deriv_x, deriv_x_i = 1, 1
        deriv_y, y_i = 2, 2
        deriv_z, z_i = 3, 3

        # Solve
        derivs[ODEIndex.x] = deriv_x
        derivs[ODEIndex.y] = deriv_y
        derivs[ODEIndex.z] = deriv_z

    return rhs_equation





