# Contains the functions to solve the model given from models.py

from DEModelling.models.one_var import *
from DEModelling.utils import ODEIndex
from DEModelling.data_format import InternalData

from numpy import copy

unsed_model = 0, 0

def ode_system(*, store_internal_data=True):
    """
        Create the mathematical ODE model.
        Returns the sundials ode model which will be solved.
    """

    # The internal data allows the user to obtain the solved values of any variable they want at each time step.
    if store_internal_data:
        internal_data = InternalData()
        times_list = internal_data.times
        params_list = internal_data.params
        derivs_list = internal_data.derivs
        x1_list = internal_data.x1
        x2_list = internal_data.x2
        x3_list = internal_data.x3
        x1dot_list = internal_data.x1dot
        x2dot_list = internal_data.x2dot
        x3dot_list = internal_data.x3dot
        x1ddot_list = internal_data.x1ddot
        x2ddot_list = internal_data.x2ddot
        x3ddot_list = internal_data.x3ddot
        problems = internal_data.problems
    else:
        internal_data = None

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
        x1ddot = params[ODEIndex.x1ddot]
        x2ddot = params[ODEIndex.x2ddot]
        x3ddot = params[ODEIndex.x3ddot]

        # First order derivative functions
        # Place here the RHS of the equation.
        # i.e. x' = 2x + 3 would be deriv_x = model_2x1_plus_3_func()
        deriv_x1, x1_i = model_x1_func(x1=x1)
        deriv_x2, x2_i = model_x2_func(x2=x2)
        deriv_x3, x3_i = model_x3_func(x3=x3)
        deriv_x1dot, x1dot_i = unsed_model
        deriv_x2dot, x2dot_i = unsed_model
        deriv_x3dot, x3dot_i = unsed_model
        deriv_x1ddot, x1ddot_i = unsed_model
        deriv_x2ddot, x2ddot_i = unsed_model
        deriv_x3ddot, x3ddot_i = unsed_model

        # Solve
        derivs[ODEIndex.x1] = deriv_x1
        derivs[ODEIndex.x2] = deriv_x2
        derivs[ODEIndex.x3] = deriv_x3

        if store_internal_data:
            params_list.append(copy(params))
            derivs_list.append(copy(derivs))
            times_list.append(copy(time))
            x1_list.append(copy(x1_i))
            x2_list.append(copy(x2_i))
            x3_list.append(copy(x3_i))
            x1dot_list.append(copy(x1dot_i))
            x2dot_list.append(copy(x2dot_i))
            x3dot_list.append(copy(x3dot_i))
            x1ddot_list.append(copy(x1ddot_i))
            x2ddot_list.append(copy(x2ddot_i))
            x3ddot_list.append(copy(x3ddot_i))


    return rhs_equation, internal_data





