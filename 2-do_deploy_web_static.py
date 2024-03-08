#!/usr/bin/env python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric import task
from datetime import datetime
import os

# Define the user and host addresses for your web servers
env.user = 'ubuntu'
env.hosts = ['3.235.24.147', '34.203.38.9']


@task
def do_deploy(c, archive_path):
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

        # Upload the archive to /tmp directory of the web server
        c.put(archive_path, "/tmp/")

        # Create directory for the new version
        c.run("mkdir -p /data/web_static/releases/{}/".format(filename_no_ext))

        # Uncompress the archive to the specified directory
        c.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
              .format(filename, filename_no_ext))

        # Delete the archive from the web server
        c.run("rm /tmp/{}".format(filename))

        # Move contents of the uncompressed directory to parent directory
        c.run("mv /data/web_static/releases/{}/web_static/* \
              /data/web_static/releases/{}/"
              .format(filename_no_ext, filename_no_ext))

        # Remove the now empty web_static directory
        c.run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename_no_ext))

        # Delete the symbolic link /data/web_static/current
        c.run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version
        c.run("ln -s /data/web_static/releases/{}/ \
              /data/web_static/current"
              .format(filename_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error:", e)
        return False
