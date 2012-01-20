import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/django-deployment/')))
from fabric.api import env
from deployment import DeploymentConfig
 
config = DeploymentConfig(__file__)
#config.domains[config.ENVTYPE_STAGING] = ['staging.freiheitsfreunde.net','ffs.h1668526.stratoserver.net']
#config.domains[config.ENVTYPE_PRODUCTION] = ['freiheitsfreunde.net', 'ff.h1668526.stratoserver.net']
#config.add_action('create', 'conf',)
#config.add_action('create', 'var',)
#config.add_action('create', 'var/db', owner=DeploymentConfig.USER_WEBSERVER)
#config.add_action('rsync', 'proj',)
#config.add_action('compile', 'proj',)
#config.add_action('create', 'media',)
#config.add_action('link-admin-media', None)
#config.add_action('rsync', 'media/js',)
#config.add_action('rsync', 'media/css',)
#config.add_action('rsync', 'media/img',)
#config.add_action('create', 'log', owner=DeploymentConfig.USER_WEBSERVER)

def deploy(env_type):
    """
    usage fab -H servername deploy:P
    """
    config.update_env(env, env_type)
    config.bootstrap_server()    
    config.update_requirements()
    config.do_actions()
    config.configure()    
