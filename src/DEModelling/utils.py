from enum import IntEnum


class ODEIndex(IntEnum):
    """
    Enumerated number for array index for variables in the ODEs
    """
    # Dimensionful units
    a1 = 0
    a1dot = 1
    a2 = 2
    a2dot = 3
    a3 = 4
    a3dot = 5
    x = 0
    xdot = 1
    y = 2
    ydot = 3
    z = 4
    zdot = 5


class InitConIndex(IntEnum):
    """
    Enumerated number for array index for variables in the initial conditions object.
    """
    a1 = 0
    a1dot = 1
    a2 = 2
    a2dot = 3
    a3 = 4
    a3dot = 5
    x = 0
    xdot = 1
    y = 2
    ydot = 3
    z = 4
    zdot = 5


