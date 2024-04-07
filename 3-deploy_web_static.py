#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the c
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import task, local, env, put, run, runs_once
from datetime import datetime


@runs_once
def do_pack():
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(formatted_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None

"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import task, local, env, put, run
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['100.26.167.133', '54.173.97.227']


@task
def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and performs deployment steps
    Args:
        archive_path: Path to the archive to be deployed
    Returns:
        True if all operations have been done correctly, otherwise False
    """
    if not os.path.exists(archive_path):
        print("Archive doesn't exist.")
        return False

    try:
        # Extract filename from archive_path
        filename = os.path.basename(archive_path)
        filename_no_ext = filename.split('.')[0]
        dpath = "/data/web_static/releases/"
        # Upload the archive to /tmp directory of the web server
        put(archive_path, "/tmp/")
        #remove the path if it exists
        run("rm -rf {}{}/".format(dpath, filename_no_ext))

        # Create directory for the new version
        run("mkdir -p /data/web_static/releases/{}/".format(filename_no_ext))

        # Uncompress the archive to the specified directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
              .format(filename, filename_no_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move contents of the uncompressed directory to parent directory
        run("mv /data/web_static/releases/{}/web_static/* \
              /data/web_static/releases/{}/"
              .format(filename_no_ext, filename_no_ext))

        # Remove the now empty web_static directory
        run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename_no_ext))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version
        run("ln -s /data/web_static/releases/{}/ \
              /data/web_static/current"
              .format(filename_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error:", e)
        return False
    except Exception as e:
        print("Error:", e)
        return False

@task
def deploy():
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
