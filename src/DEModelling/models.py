# Main file containing the models which we seek to solve.

def model_x_deriv_func(*, x):
    """ A model where the x function changes as it's derivative.
    """
    return x, x


def model_x2_deriv_func(*, x):
    """ A model where the x function changes as it's derivative squared.
    """
    return x**2, x**2


def model_x3_deriv_func(*, x):
    """ A model where the x function changes as it's derivative cubed.
    """
    return x**3, x**3


def model_const_1_deriv_func(*, x):
    """ A model where the x function changes as 1 aslways.
    """
    return 1, 1

def model_2x_deriv_func(*, x):
    """ A model where the x function changes as it's derivative squared.
    """
    return 2*x, 2*x


def model_const_2_deriv_func(*, x):
    """ A model where the x function changes as 1 aslways.
    """
    return 2, 2



def get_model(selected_model):
    """ Returns the selected model.
    """
    print("The selected model was", selected_model)
    models = {"x":model_x_deriv_func, "x2":model_x2_deriv_func, "x3":model_x3_deriv_func, "const_1":model_const_1_deriv_func, "const_2":model_const_2_deriv_func, "2x":model_2x_deriv_func}

    return models.get(selected_model)
