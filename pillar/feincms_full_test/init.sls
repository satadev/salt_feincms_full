feincms_full_test:
    options:
        is_env_apply: True
        is_lib_apply: True
        is_opt_apply: True
        is_db_apply: True
        is_webserver_apply: True
    allowed_hosts:
        - 127.0.0.1
        - feincms-full-test.com
        - www.feincms-full-test.com
    request_ignore_ip:
        - 127.0.0.1
    blog_paginate_by: 3
    blog_title: 'Super School News'
    blog_description: 'Super School News Super Blog!'
    haystack_search_results_per_page: 10
    postgresql:
        user: feincms_full_test
        name: feincms_full_test
        pass: test
    nginx:
        server_name:
            - feincms-full-test.com
            - www.feincms-full-test.com
    gunicorn:
        num_workers: 9
