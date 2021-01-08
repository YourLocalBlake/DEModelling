# Main file containing the models which we seek to solve.

def model_x_deriv_func(*, xdot):
    """ A model where the x function changes as it's derivative.
    """
    return xdot, xdot


def model_x2_deriv_func(*, xdot):
    """ A model where the x function changes as it's derivative squared.
    """
    return xdot**2, xdot**2


def model_x3_deriv_func(*, xdot):
    """ A model where the x function changes as it's derivative cubed.
    """
    return xdot**3, xdot**3


def model_const_1_deriv_func(*, xdot):
    """ A model where the x function changes as 1 aslways.
    """
    return 1, 1
