#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    All files in the folder web_static are added to the final archive.
    All archives are stored in the folder versions.
    The name of the archive created is web_static_<year><month><day><hour><minute><second>.tgz
    Returns:
        Archive path if the archive has been correctly generated, otherwise None.
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
