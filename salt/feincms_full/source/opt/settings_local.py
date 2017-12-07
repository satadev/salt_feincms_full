{% set project_name = salt['pillar.get']('project_name') %}
{% set allowed_hosts = salt['pillar.get'](project_name + ':allowed_hosts') %}
from settings import *


#
# initial data
#
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'core/fixtures/'),
)


#
# email
#
{% include '/srv/pillar/' + project_name + '/source/opt/settings_local_email.py' %}


#
# debug
#
DEBUG = True
INTERNAL_IPS = ['127.0.0.1',]
ALLOWED_HOSTS = [{% for host in allowed_hosts %}{% if not loop.first %}, {% endif %}'{{ host }}'{% endfor %}]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE

    # activate debug_toolbar for gunicorn & nginx
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True
    }


