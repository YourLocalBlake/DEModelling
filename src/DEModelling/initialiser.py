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
        x1 = params[ODEIndex.x1]
        x2 = params[ODEIndex.x2]
        x3 = params[ODEIndex.x3]
        x1dot = params[ODEIndex.x1dot]
        x2dot = params[ODEIndex.x2dot]
        x3dot = params[ODEIndex.x3dot]

        # First order derivative functions
        # Place here the RHS of the equation.
        # i.e. x' = 2x + 3 would be deriv_x = model_2x1_plus_3_func()
        deriv_x1, x1_i = model_x1_func(x1=x1)
        deriv_x2, x2_i = model_x2_func(x2=x2)
        deriv_x3, x3_i = model_x3_func(x3=x3)

        # Solve
        derivs[ODEIndex.x1] = deriv_x1
        derivs[ODEIndex.x2] = deriv_x2
        derivs[ODEIndex.x3] = deriv_x3

    return rhs_equation





