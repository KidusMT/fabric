#(1)
#!/usr/bin/env python
# from fabric.api import local

# def update():
#     local('update')

#(2)
# from fabric.api import env, run

# env.hosts = ['34.66.135.245', '192.168.1.101', '192.168.1.102']

# def uptime():
#     run('uptime')

#(3)
from fabric.api import *
from fabric.colors import *

def install_pyp():
    local('pip2 install pyp')

def ls_upper():
    output = local('ls | pyp "p.upper()"', capture=True)
    print blue(output, bold=True)

def home_work():
    # initOutPut = local('git init')
    addOutPut = local('git add .')
    commitOutPut = local('git commit -m "commit by fab edited"')
    # remoteOutPut = local('git remote add origin https://github.com/KidusMT/fabric.git')
    pushOutPut = local('git push -u origin master')
    # print blue(initOutPut, bold=True)
    print red(addOutPut, bold=True)
    print yellow(commitOutPut, bold=True)
    # print green(remoteOutPut, bold=True)
    print green(pushOutPut, bold=True)