#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    # Compress the web_static folder into a .tgz archive
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
