import os
from contextlib import contextmanager as _contextmanager

from fabric.api import (abort, cd, env, local, prefix, prompt, run, settings,
                        task)
from fabric.colors import cyan, green, red
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
import datetime
import sys

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
    date= datetime.datetime.now().strftime("%d%m%Y")
    with settings(warn_only=True, host_string=SERV_MAPPING[server]):
        run('rm -rf %s.%s'%(PROJECT_PATH_MAPPING[server], 'old'))
        run('cp -rf %s %s.%s'%(PROJECT_PATH_MAPPING[server], PROJECT_PATH_MAPPING[server], 'old'))

@task
def restore_directories(server=PROD):
    """
    restore directories
    """
    print_title_task('restore server directories %s' % server.upper())
    date= datetime.datetime.now().strftime("%d%m%Y")
    with settings(warn_only=True, host_string=SERV_MAPPING[server]):
        run('rm -rf %s'%PROJECT_PATH_MAPPING[server])
        run('cp -rf %s.%s %s'%(PROJECT_PATH_MAPPING[server], 'old', PROJECT_PATH_MAPPING[server]))
        
@task
def pull(server=PROD):
    """
    Pull last commit on target server
    """
    print_title_task('Pull source code on server %s' % server.upper())
    with settings(warn_only=True, host_string=SERV_MAPPING[server]):
        with cd(PROJECT_PATH_MAPPING[server]):
            run('git checkout %s' % BRANCH_MAPPING[server])
            run('git pull')

@task
def install_dependencies(server=PROD):
    """
    Install dependencies on target server
    """
    print_title_task('Install dependencies on server %s' % server.upper())
    with settings(warn_only=True, host_string=SERV_MAPPING[server]):
        with cd(PROJECT_PATH_MAPPING[server]):
            with virtualenv(server):
                branch = BRANCH_MAPPING_BASE[server]
                run('pip install -r requirements.txt')

@task
def restart_server(server=PROD):
    """
    Restart the target server
    """
    print_title_task('Restart server %s' % server.upper())
    server_names = SERVER_MAPPING[server]
    with settings(warn_only=True, host_string=SERV_MAPPING[server]):
        run('supervisorctl restart %s' % server_names)  # Depending arch, will see that later
