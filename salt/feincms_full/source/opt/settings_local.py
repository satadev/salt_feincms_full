{% set project_name = salt['pillar.get']('project_name') %}

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


