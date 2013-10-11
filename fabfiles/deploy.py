from fabric.api import *
from fabric.operations import sudo, put
from fabric.context_managers import cd, prefix
from fabric.contrib import files
import os

env.hosts = ['star']
env.use_ssh_config = True

WWW_DIR = '/home/starsirius'
WWW_USER = 'www-data'
REPOS = {
    'star': 'starsirius'
}
VENV_PATH = os.path.join(WWW_DIR, REPOS['star'], 'starenv')
LIBS_PATH = os.path.join(VENV_PATH, 'local/lib/python2.7')
PYTHON_PATH = os.path.join(VENV_PATH, 'bin/python')
#MGR_PATH = os.path.join(WWW_DIR, REPOS['deux'], 'src/deux/deux/manager.py')
#STATIC_PATH = os.path.join(WWW_DIR, REPOS['deux'], 'static')

def __fetch_latest_release():
    run('git checkout master && git pull origin master')

def __install_star_package():
    with cd(os.path.join(WWW_DIR, REPOS['star'], 'src/star')):
        with prefix('source ../../starenv/bin/activate'):
            run('python setup.py develop')

def __install_requirements(requirements_filename='requirements.txt', download=True):
    """Downloads packages from pypi and installs them.
        Arguments:
            download - a boolean, whether to get the packages again (True) or only to install
            packages cached on the host this method is targeting (False). [True]
    """
    with cd(os.path.join(WWW_DIR, REPOS['star'])):
        if not files.exists('starenv'):
            run('virtualenv --distribute starenv')
        with prefix('source starenv/bin/activate'):
            #sudo('python src/deux/setup.py install') # Versioned package - can be used with a release server at some point
            run('pip install {} -r {}'.format('' if download else '--no-download', requirements_filename))

def __restart_services(*services):
    for s in services:
        """
        if s == 'uwsgi': # hack until we fix process spawning
            with settings(warn_only=True):
                sudo("ps -ef | grep uwsgi | awk '{print $2}'| xargs kill -9")
        """
        sudo('service {} restart'.format(s)) # Generally the service will have a restart command

def __reload_services(*services):
    for s in services:
        sudo('service {} reload'.format(s))

@task
def deploy(release_branch='master', www_dir=WWW_DIR, www_user=WWW_USER):
    """Run the latest code, SQL paches and manager migration tools on this server.
    """
    with cd(www_dir):
        with cd(REPOS['star']):
            __fetch_latest_release()
            __install_star_package()
            __install_requirements()
            #__install_custom_modules()
            with cd('src/star/star'):
                with prefix('source ../../../starenv/bin/activate'):
                    #run('python manager.py assets build -c ../prod.ini', user='www-data')
                    #run('alembic -c alembic_prod.ini upgrade head')
            #__link_config_files('development.ini', 'stage.ini', 'prod.ini') # If using versioned packages / setup.py install
            __restart_services('nginx', 'uwsgi')
            #__reload_services('uwsgi')
