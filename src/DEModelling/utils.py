from enum import IntEnum


class ODEIndex(IntEnum):
    """
    Enumerated number for array index for variables in the ODEs
    """
    # Dimensionful units
    x1 = 0
    x1dot = 1
    x1ddot = 2
    x2 = 3
    x2dot = 4
    x2ddot = 5
    x3 = 6
    x3dot = 7
    x3ddot = 8
    x4 = 9
    x4dot = 10
    x5 = 11
    x5dot = 12
    x5ddot = 13


class InitConIndex(IntEnum):
    """
    Enumerated number for array index for variables in the initial conditions object.
    """
    x1 = 0
    x1dot = 1
    x1ddot = 2
    x2 = 3
    x2dot = 4
    x2ddot = 5
    x3 = 6
    x3dot = 7
    x3ddot = 8
    x4 = 9
    x4dot = 10
    x5 = 11
    x5dot = 12
    x5ddot = 13


