import sys


from conda.common.compat import ensure_text_type
from conda.base.context import context
from conda.cli.main import init_loggers
from conda.activate import _build_activator_cls

import conda.plugins


def handle_env(*args, **kwargs):
    # cleanup argv
    env_args = sys.argv[2:]  # drop executable/script and sub-command
    env_args = tuple(ensure_text_type(s) for s in env_args)

    context.__init__()
    init_loggers(context)

    
    activator_cls = _build_activator_cls('bash') # TODO: take this out and just put the PosixActivator
    
    activator = activator_cls(env_args)
    print(activator.execute(), end="")
    print("echo The power is yours!") # confirm that we're using plugin and not usual conda process

    return sys.exit(0)

@conda.plugins.hookimpl
def conda_subcommands():
    yield conda.plugins.CondaSubcommand(
        name="captain-planet",
        summary="Plugin for POSIX shells that calls the conda processes used for activate, deactivate, reactivate, hook, and command",
        action=handle_env,
    )