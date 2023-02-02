#!/usr/bin/python3
""" Function that deploys """
from datetime import datetime
from fabric.api import *
import os
import shlex


rom fabric.api import put, run, env, sudo
from os.path import exists
env.hosts = ['54.82.132.243', '54.157.160.87']
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"
env.password = "betty"


def deploy():
    """ DEPLOYS """
    try:
        archive_path = do_pack()
    except:
        return False

    return do_deploy(archive_path)


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """ Deploys """
    if not os.path.exists(archive_path):
        return False
    try:
