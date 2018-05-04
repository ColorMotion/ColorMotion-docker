import os
import subprocess


def parse_environment(environment):
    '''Build a dictionary from the env command output.'''
    key_values = [x.partition('=') for x in environment.splitlines()]
    return {key: value for key, _, value in key_values if key}


def bash_env(filename):
    '''Run source && env in bash and return its output.'''
    return parse_environment(subprocess.check_output([
        'bash', '-c', 'source {} && env'.format(filename)
    ], universal_newlines=True))


def bash_source(filename):
    '''Update the current process' environment with bash's source command.'''
    os.environ.update(bash_env(filename))
