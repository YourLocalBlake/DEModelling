"""
Load phy5 files
"""
import h5py

from DEModelling.data_format import Solution, ConfigParams, InitialConditions, InternalData


def solution_loader(file_name=None):
    """
    Load a hdf5 file containing a solved ODE
    Returns the 4 data objects
    """
    if file_name is not None:
        import os
        print("cwd", os.getcwd())
        try:
            h5py.File(file_name, "r")
        except OSError:
            try:
                file_name = file_name + ".hdf5"
                h5py.File(file_name, "r")
            except OSError:
                raise SystemExit("Could not find file, got {}".format(file_name))
    else:
        raise SystemExit("No file given, got {}".format(file_name))

    with h5py.File(file_name, "r") as f:
        solution = Solution(
            solution=f["solution"]["solution"][:],
            times=f["solution"]["times"][:],
            flags=f["solution"]["flags"][:],
            tstop_times=f["solution"].attrs["tstop_times"],
            jump_times=f["solution"].attrs["jump_times"]
        )

        config_params = ConfigParams(
            start=f["solver_config"].attrs["start"],
            stop=f["solver_config"].attrs["stop"],
            num_time=f["solver_config"].attrs["num_time"],
            max_steps=f["solver_config"].attrs["max_steps"],
            relative_tolerance=f["solver_config"].attrs["relative_tolerance"],
            absolute_tolerance=f["solver_config"].attrs["absolute_tolerance"],
            enable_tstop=f["solver_config"].attrs["enable_tstop"],
            tstop_times=f["solver_config"].attrs["tstop_times"]
        )

        internal_data = InternalData(
            params=f["internal_data"]["params"][:],
            derivs=f["internal_data"]["derivs"][:],
            times=f["internal_data"]["times"][:],
            x1=f["internal_data"]["x1"][:],
            x1dot=f["internal_data"]["x1dot"][:],
            x1ddot=f["internal_data"]["x1ddot"][:],
            x2=f["internal_data"]["x2"][:],
            x2dot=f["internal_data"]["x2dot"][:],
            x2ddot=f["internal_data"]["x2ddot"][:],
            x3=f["internal_data"]["x3"][:],
            x3dot=f["internal_data"]["x3dot"][:],
            x3ddot=f["internal_data"]["x3ddot"][:],
            problems=f["internal_data"].attrs["problems"]
        )

        initial_conditions = InitialConditions(
            init_x1=f["initial_conditions"].attrs["init_x1"],
            init_x2=f["initial_conditions"].attrs["init_x2"],
            init_x3=f["initial_conditions"].attrs["init_x3"],
            init_x1dot=f["initial_conditions"].attrs["init_x1dot"],
            init_x2dot=f["initial_conditions"].attrs["init_x2dot"],
            init_x3dot=f["initial_conditions"].attrs["init_x3dot"],
            init_x1ddot=f["initial_conditions"].attrs["init_x1ddot"],
            init_x2ddot=f["initial_conditions"].attrs["init_x2ddot"],
            init_x3ddot=f["initial_conditions"].attrs["init_x3ddot"]
        )

    return solution, initial_conditions, config_params, internal_data
