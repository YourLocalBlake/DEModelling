"""
Define the data structures used.
"""
import attr


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


