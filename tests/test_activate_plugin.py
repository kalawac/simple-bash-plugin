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

def test_default_env():
    activator = PosixActivator()
    assert ROOT_ENV_NAME == activator._default_env(context.root_prefix)

    with tempdir() as td:
        assert td == activator._default_env(td)

        p = mkdir_p(join(td, "envs", "named-env"))
        assert "named-env" == activator._default_env(p)

