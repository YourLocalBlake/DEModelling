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


def model_x1_func(*, x1):
    """ A model where the x1 derivative changes as x1.
    """
    return x1, x1


def model_x1_deriv_func(*, x1dot):
    """ A model where the x1 derivative changes as the derivative of the x1 function.
    """
    return x1dot, x1dot


def model_x1_squared_func(*, x1):
    """ A model where the x1 derivative changes as x1 squared.
    """
    return x1**2, x1**2


def model_x1_squared_deriv_func(*, x1dot):
    """ A model where the x1 derivative changes as the derivative of the x1 function squared.
    """
    return x1dot**2, x1dot**2


def model_x1_cubed_func(*, x1):
    """ A model where the x1 derivative changes as x1 cubed.
    """
    return x1**3, x1**3


def model_x1_cubed_deriv_func(*, x1dot):
    """ A model where the x1 derivative changes as the derivative of the x1 function cubed.
    """
    return x1dot**3, x1dot**3


def model_2x1_func(*, x1):
    """ A model where the x1 derivative changes as 2 times x1.
    """
    return 2*x1, 2*x1


def model_2x1_deriv_func(*, x1dot):
    """ A model where the x1 derivative changes as 2 times the derivative of the x1 function.
    """
    return 2*x1dot, 2*x1dot


def model_x2_func(*, x2):
    """ A model where the x2 derivative changes as x2.
    """
    return x2, x2


def model_x2_deriv_func(*, x2dot):
    """ A model where the x2 derivative changes as the derivative of the x2 function.
    """
    return x2dot, x2dot


def model_x2_squared_func(*, x2):
    """ A model where the x2 derivative changes as x2 squared.
    """
    return x2**2, x2**2


def model_x2_squared_deriv_func(*, x2dot):
    """ A model where the x2 derivative changes as the derivative of the x2 function squared.
    """
    return x2dot**2, x2dot**2


def model_x2_cubed_func(*, x2):
    """ A model where the x2 derivative changes as x2 cubed.
    """
    return x2**3, x2**3


def model_x2_cubed_deriv_func(*, x2dot):
    """ A model where the x2 derivative changes as the derivative of the x2 function cubed.
    """
    return x2dot**3, x2dot**3


def model_2x_squared_func(*, x2):
    """ A model where the x2 derivative changes as 2 times x2.
    """
    return 2*x2, 2*x2


def model_2x2_deriv_func(*, x2dot):
    """ A model where the x2 derivative changes as 2 times the derivative of the x2 function.
    """
    return 2*x2dot, 2*x2dot


def model_x3_func(*, x3):
    """ A model where the derivative changes as x3.
    """
    return x3, x3


def model_x3_deriv_func(*, x3dot):
    """ A model where the derivative changes as the derivative of the x3 function.
    """
    return x3dot, x3dot


def model_x3_squared_func(*, x3):
    """ A model where the derivative changes as x3 squared.
    """
    return x3**2, x3**2


def model_x3_squared_deriv_func(*, x3dot):
    """ A model where the derivative changes as the derivative of the x3 function squared.
    """
    return x3dot**2, x3dot**2


def model_x3_cubed_func(*, x3):
    """ A model where the derivative changes as x3 cubed.
    """
    return x3**3, x3**3


def model_x3_cubed_deriv_func(*, x3dot):
    """ A model where the derivative changes as the derivative of the x3 function cubed.
    """
    return x3dot**3, x3dot**3


def model_2x3_func(*, x3):
    """ A model where the derivative changes as 2 times x3.
    """
    return 2*x3, 2*x3


def model_2x3_deriv_func(*, x3dot):
    """ A model where the derivative changes as 2 times the derivative of the x3 function.
    """
    return 2*x3dot, 2*x3dot
