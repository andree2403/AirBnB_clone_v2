#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['52.87.216.236', '100.26.171.103']  # Replace with the IP address or hostname of your web server
env.user = 'ubuntu'  # Replace with your SSH username
env.key_filename = '/home/vagrant/.ssh/school'  # Replace with the path to your private key file


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

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace('.tgz', "")
    folder_path = '/data/web_static/releases/{}/'.format(folder_name) 
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}".format(folder_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, folder_path))
        run('sudo rm -rf /tmp/{}'.format(file_name))
        run('sudo mv -f {}web_static/* {}'.format(folder_path, folder_path))
        run("sudo rm -rf {}web_static".format(folder_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(folder_path))
    except Exception:
        return False
    return True

def deploy():
    """creates and distributes an archive to your web servers, using deploy"""
    archive = do_pack()
    if archive is None:
        return False
    else:
        return do_deploy(archive)

