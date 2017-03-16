import os
from contextlib import contextmanager as _contextmanager

from fabric.api import (abort, cd, env, local, prefix, prompt, run, settings,
                        task)
from fabric.colors import cyan, green, red
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
import datetime
import sys

run('cp -rf %s %s.%s'%(PROJECT_PATH_MAPPING[server], PROJECT_PATH_MAPPING[server], new_date))
run('pip install -r requirements.txt')
run('git pull')
local('git commit -am "Update version to %s"' % new_version)
cd(path)
