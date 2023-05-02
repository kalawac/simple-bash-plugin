import pytest
from os.path import dirname, isdir, join

from conda.activate import (
    PosixActivator,
    activator_map,
    native_path_to_unix,
)
from conda.base.constants import (
    CONDA_ENV_VARS_UNSET_VAR,
    PACKAGE_ENV_VARS_DIR,
    PREFIX_STATE_FILE,
    ROOT_ENV_NAME,
)
from conda.testing.helpers import tempdir
from conda.gateways.disk.create import mkdir_p

from conda.base.context import conda_tests_ctxt_mgmt_def_pol, context

@pytest.fixture(autouse=True)
def activator():
    activator = PosixActivator()
    activator._default_env(context.root_prefix)

def test_default_env(activator):
    assert ROOT_ENV_NAME == activator

    with tempdir() as td:
        assert td == activator._default_env(td)

        p = mkdir_p(join(td, "envs", "named-env"))
        assert "named-env" == activator._default_env(p)

# """
# Using this file to check the conda env created in bash
# """
# #Constants
# CONDA_ENV_VERSION =  "23.0.1"
# CONDA_ENV_LOCATION = "./<conda_project>/plugin"
# test_activate()
# """ The test cases activates the conda env
# conda activate env
# assert conda env return not none (Unit)
# run conda info
# assert
#         a. CONDA Version
#         b. CONDA Location
#         c. CONDA dependcies is not None
# """
# # Ran the conda activate..
# # Run conda info
# # Run command |grep "env_info.txt"
# # file reader(env_info.txt)
#     with reading the file line by line
#     assert "Constansts"
#     assert f"conda_dependecies" is not None
# ```


# OLD
# def test_default_env():
#     activator = PosixActivator()
#     assert ROOT_ENV_NAME == activator._default_env(context.root_prefix)

#     with tempdir() as td:
#         assert td == activator._default_env(td)

#         p = mkdir_p(join(td, "envs", "named-env"))
#         assert "named-env" == activator._default_env(p)

