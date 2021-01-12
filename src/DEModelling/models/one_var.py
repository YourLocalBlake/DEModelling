# Main file containing one dimensional derivatives.

def model_const_0_func():
    """ A model where the derivative changes as constant 1.
    """
    return 0, 0

def model_const_1_func():
    """ A model where the derivative changes as constant 1.
    """
    return 1, 1


def model_const_2_func():
    """ A model where the derivative changes as constant 2.
    """
    return 2, 2


def model_x_func(*, x):
    """ A model where the x derivative changes as x.
    """
    return x, x


def model_x_deriv_func(*, xdot):
    """ A model where the x derivative changes as the derivative of the x function.
    """
    return xdot, xdot


def model_x2_func(*, x):
    """ A model where the x derivative changes as x squared.
    """
    return x**2, x**2


def model_x2_deriv_func(*, xdot):
    """ A model where the x derivative changes as the derivative of the x function squared.
    """
    return xdot**2, xdot**2


def model_x3_func(*, x):
    """ A model where the x derivative changes as x cubed.
    """
    return x**3, x**3


def model_x3_deriv_func(*, xdot):
    """ A model where the x derivative changes as the derivative of the x function cubed.
    """
    return xdot**3, xdot**3


def model_2x_func(*, x):
    """ A model where the x derivative changes as 2 times x.
    """
    return 2*x, 2*x


def model_2x_deriv_func(*, xdot):
    """ A model where the x derivative changes as 2 times the derivative of the x function.
    """
    return 2*xdot, 2*xdot


def model_y_func(*, y):
    """ A model where the y derivative changes as y.
    """
    return y, y


def model_y_deriv_func(*, ydot):
    """ A model where the y derivative changes as the derivative of the y function.
    """
    return ydot, ydot


def model_y2_func(*, y):
    """ A model where the y derivative changes as y squared.
    """
    return y**2, y**2


def model_y2_deriv_func(*, ydot):
    """ A model where the y derivative changes as the derivative of the y function squared.
    """
    return ydot**2, ydot**2


def model_y3_func(*, y):
    """ A model where the y derivative changes as y cubed.
    """
    return y**3, y**3


def model_y3_deriv_func(*, ydot):
    """ A model where the y derivative changes as the derivative of the y function cubed.
    """
    return ydot**3, ydot**3


def model_2y_func(*, y):
    """ A model where the y derivative changes as 2 times y.
    """
    return 2*y, 2*y


def model_2y_deriv_func(*, ydot):
    """ A model where the y derivative changes as 2 times the derivative of the y function.
    """
    return 2*ydot, 2*ydot


def model_z_func(*, z):
    """ A model where the derivative changes as z.
    """
    return z, z


def model_z_deriv_func(*, zdot):
    """ A model where the derivative changes as the derivative of the z function.
    """
    return zdot, zdot


def model_z2_func(*, z):
    """ A model where the derivative changes as z squared.
    """
    return z**2, z**2


def model_z2_deriv_func(*, zdot):
    """ A model where the derivative changes as the derivative of the z function squared.
    """
    return zdot**2, zdot**2


def model_z3_func(*, z):
    """ A model where the derivative changes as z cubed.
    """
    return z**3, z**3


def model_z3_deriv_func(*, zdot):
    """ A model where the derivative changes as the derivative of the z function cubed.
    """
    return zdot**3, zdot**3


def model_2z_func(*, z):
    """ A model where the derivative changes as 2 times z.
    """
    return 2*z, 2*z


def model_2z_deriv_func(*, zdot):
    """ A model where the derivative changes as 2 times the derivative of the z function.
    """
    return 2*zdot, 2*zdot

