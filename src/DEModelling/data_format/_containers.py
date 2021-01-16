"""
Define the data structures used.
"""
import attr
from numpy import asarray, concatenate
from DEModelling.utils import ODEIndex

@attr.s
class InitialConditions:
    """
    Datastructure for the initial conditions of the system and ODE
    """
    # A better way to do this is to only have the required ones and make the user initialse them all.
    init_x1 = attr.ib(default=0, type=attr.Factory(int))
    init_x1dot = attr.ib(default=0, type=attr.Factory(int))
    init_x1ddot = attr.ib(default=0, type=attr.Factory(int))
    init_x2 = attr.ib(default=0, type=attr.Factory(int))
    init_x2dot = attr.ib(default=0, type=attr.Factory(int))
    init_x2ddot = attr.ib(default=0, type=attr.Factory(int))
    init_x3 = attr.ib(default=0, type=attr.Factory(int))
    init_x3dot = attr.ib(default=0, type=attr.Factory(int))
    init_x3ddot = attr.ib(default=0, type=attr.Factory(int))
    ode_init_con = attr.ib(init=False, default=attr.Factory(list))

    def __attrs_post_init__(self):
        self.ode_init_con = [self.init_x1, self.init_x1dot, self.init_x1ddot, self.init_x2, self.init_x2dot,
                             self.init_x2ddot, self.init_x3, self.init_x3dot, self.init_x3ddot]
        # Order corresponds to order of ENum.


@attr.s
class ConfigParams:
    """
    Datastructure for the runtime configuration options.
    """
    start = attr.ib()
    stop = attr.ib()
    num_time = attr.ib()
    max_steps = attr.ib()
    relative_tolerance = attr.ib()
    absolute_tolerance = attr.ib()
    enable_tstop = attr.ib()
    tstop_times = attr.ib(default=attr.Factory(list))


@attr.s
class Solution:
    """
    Datastructure of solutions.
    """
    times = attr.ib()
    solution = attr.ib()
    flags = attr.ib(default=attr.Factory(list))
    tstop_times = attr.ib(default=attr.Factory(list))
    jump_times = attr.ib(default=attr.Factory(list))


@attr.s
class InternalData:
    """
    Datastructure for internally solved params
    """
    params = attr.ib(default=attr.Factory(list))
    derivs = attr.ib(default=attr.Factory(list))
    times = attr.ib(default=attr.Factory(list))
    x1 = attr.ib(default=attr.Factory(list))
    x1dot = attr.ib(default=attr.Factory(list))
    x1ddot = attr.ib(default=attr.Factory(list))
    x2 = attr.ib(default=attr.Factory(list))
    x2dot = attr.ib(default=attr.Factory(list))
    x2ddot = attr.ib(default=attr.Factory(list))
    x3 = attr.ib(default=attr.Factory(list))
    x3dot = attr.ib(default=attr.Factory(list))
    x3ddot = attr.ib(default=attr.Factory(list))
    problems = attr.ib(default=attr.Factory(list))

    def _finalise(self):
        """
        Finalise data for storage in hdf5 files
        """
        self.derivs = asarray(self.derivs)
        if self.derivs.size == 0:
            self.derivs.shape = (0, len(ODEIndex))

        self.params = asarray(self.params)
        if self.params.size == 0:
            self.params.shape = (0, len(ODEIndex))

        self.times = asarray(self.times)
        self.x1 = asarray(self.x1)
        self.x1dot = asarray(self.x1dot)
        self.x1ddot = asarray(self.x1ddot)
        self.x2 = asarray(self.x2)
        self.x2dot = asarray(self.x2dot)
        self.x2ddot = asarray(self.x2ddot)
        self.x3 = asarray(self.x3)
        self.x3dot = asarray(self.x3dot)
        self.x3ddot = asarray(self.x3ddot)

    def __add__(self, other):
        """
        This is required for adding two internal data sets together
        """
        self._finalise()
        other._finalise()

        return InternalData(
            derivs=concatenate((self.derivs, other.derivs)),
            params=concatenate((self.params, other.params)),
            times=concatenate((self.times, other.times)),
            x1=concatenate((self.x1, other.x1)),
            x1dot=concatenate((self.x1dot, other.x1dot)),
            x1ddot=concatenate((self.x1ddot, other.x1ddot)),
            x2=concatenate((self.x2, other.x2)),
            x2dot=concatenate((self.x2dot, other.x2dot)),
            x2ddot=concatenate((self.x2ddot, other.x2ddot)),
            x3=concatenate((self.x3, other.x3)),
            x3dot=concatenate((self.x3dot, other.x3dot)),
            x3ddot=concatenate((self.x3ddot, other.x3ddot)),
            problems=self.problems + other.problems,
        )
