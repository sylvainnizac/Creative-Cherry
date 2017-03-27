import os
from contextlib import contextmanager as _contextmanager

from fabric.api import (abort, cd, env, local, prefix, prompt, run, settings,
                        task)
from fabric.colors import cyan, green, red
from fabric.contrib.console import confirm
from fabric.contrib.files import existslog
import sys

PROD = "prod"
PROJECT_NAME = "Creative-Cherry"


def print_title_task(title):
    length = len(title)
    print(cyan('-' * length))
    print(cyan(title))
    print(cyan('-' * length))


@task
def deploy(server=PROD):
    """
    Deploy code for target server, install dependencies and restart server
    """
    print_title_task('Deploy on server %s' % server.upper())
    question = red('Do you really want to deploy on server ') + red('%s' % server.upper(), True) + red('?')
    if confirm(question, default=False):
        save_directories(server)
        pull(server)
        install_dependencies(server)
        restart_server(server)


@task
def rollback(server=PROD):
    """
    Rollback code for target server, restart server
    """
    print_title_task('Rollback on server %s' % server.upper())
    question = red('Do you really want to rollback on server ') + red('%s' % server.upper(), True) + red('?')
    if confirm(question, default=False):
        restore_directories(server)
        restart_server(server)


@task
def save_directories(server=PROD):
    """
    save directories
    """
    print_title_task('save server directories %s' % server.upper())
    with settings(warn_only=True):
        run('rm -rf %s.%s' % (PROJECT_NAME, 'old'))
        run('cp -rf %s %s.%s' % (PROJECT_NAME, PROJECT_NAME, 'old'))


@task
def restore_directories(server=PROD):
    """
    restore directories
    """
    print_title_task('restore server directories %s' % server.upper())
    with settings(warn_only=True):
        run('rm -rf %s' % PROJECT_NAME)
        run('cp -rf %s.%s %s' % (PROJECT_NAME, 'old', PROJECT_NAME))


@task
def pull(server=PROD):
    """
    Pull last commit on target server
    """
    print_title_task('Pull source code on server %s' % server.upper())
    with settings(warn_only=True):
        with cd(PROJECT_NAME):
            run('git checkout master')
            run('git pull')


@task
def install_dependencies(server=PROD):
    """
    Install dependencies on target server
    """
    print_title_task('Install dependencies on server %s' % server.upper())
    with settings(warn_only=True):
        with cd(PROJECT_NAME):
            run('pip install -r requirements.txt')


@task
def restart_server(server=PROD):
    """
    Restart the target server
    """
    print_title_task('Restart server %s' % server.upper())
    with settings(warn_only=True):
        # Depending arch, will see that later
        run('supervisorctl restart %s' % server_names)
