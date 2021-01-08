# Contains the functions to solve the model given from models.py

from DEModelling.models import *
from DEModelling.utils import ODEIndex


def ode_system_1_var(*, x, model):
    """
        Create the mathematical ODE model.
        Returns the sundials ode model which will be solved.
    """
    model_to_use = get_model(selected_model=model)

    def rhs_equation(time, params, derivs):
        """
        RHS of the ODE equations
        Inputs are passed by Sundials.
        """
        x = params[ODEIndex.x]
        xdot = params[ODEIndex.xdot]

        # First order derivative functions

        deriv_x, deriv_x_i = model_to_use(x=x)  # x_i is implemented in later ode systems as an example of tracking internal data.

        derivs[ODEIndex.x] = deriv_x

    return rhs_equation


