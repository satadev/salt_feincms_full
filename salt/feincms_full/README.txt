
Environment
    * Debian 9
    * Salt 2016.11.2
    * Python 2.7.13
    * Django 1.11.4
    * FeinCMS 1.13.4
    * PostgreSQL 9.6
    * Nginx 1.10.3
    * Supervisor 3.3.1

    * see `/srv/pillar/feincms_full.sls` for a list of required packages

Requirements
    * see `/srv/salt/feincms_full/source/opt/requirements.txt`

Options
    * see `/srv/pillar/feincms_full_test.sls` for a list of available parameters and options

Description
    This is a Salt application that will bootstrap and teardown a FeinCMS Django project along with various FeinCMS plugins, a PostgreSQL database, Supervisor, Gunicorn, and Nginx.  Template files are omitted (for now)

    The Salt directives are straight-forward, and the nomenclature is self-explanatory.  Otherwise, questions, comments, or suggestions are always welcome.

    Following is a basic outline of the process.  See the corresponding statefile comments for further descriptions.

Process Outlines
    * bootstrap
        * env
            * update
            * setup (base)
            * setup (project)
        * lib
            * virtualenv
                * update
                * setup
                * create
                * init
        * opt
            * init
            * filestructure and initial data files
            * settings.py
            * urls.py
            * 'core' application files and settings
            * static files init
            * requirements.txt
        * db
            * db user create
            * db create
            * db settings
            * db init
        * webserver
            * gunicorn
            * supervisor
            * nginx
            * restart services
            * update host file
        * manual steps
            # supervisor restart may fail
                * `sudo service supervisor restart`
            # admin user credentials
                # user: admin
                # pass: test1234

    * teardown
        * services
            * nginx
            * supervisor
            * gunicorn
            * restart services
        * db
            * db
            * db_user
        * lib
            * rmvirtualenv
        * opt
            * rmdir

Commands
    sudo salt kali state.apply feincms_full.bootstrap \
        pillar="{ \
            project_name: 'feincms_full_test', \
            admin_user: 'dred', \
        }"
    sudo salt kali state.apply feincms_full.teardown \
        pillar="{ \
            project_name: 'feincms_full_test', \
            admin_user: 'dred', \
        }"
