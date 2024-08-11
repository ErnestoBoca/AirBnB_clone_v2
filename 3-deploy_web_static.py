#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""


from fabric.api import local, put, run, env
from os.path import isdir, exists
from datetime import datetime


def do_pack():
    """creates a version of the project"""
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


env.hosts = ["100.26.157.87", "35.174.184.63"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        archive_file = archive_path.split('/')[-1]
        file_no_ext = archive_file.split('.')[0]
        dest_folder = "/data/web_static/releases/{}/".format(file_no_ext)

        put(archive_path, '/tmp')
        run("mkdir -p {}".format(dest_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, dest_folder))
        run("rm /tmp/{}".format(archive_file))
        run("mv {0}web_static/* {0}".format(dest_folder))
        run("rm -rf {}web_static".format(dest_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_folder))
        return True
    except:
        return False


def deploy():
    """reates and distributes an archive to your the servers
    using the function deploy"""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
