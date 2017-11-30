# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from core.utils import get_meta_keywords, get_meta_description


def default(request):
    current_site = get_current_site(request)

    return {
        'SITE_URL': current_site.domain,
        'SITE_TITLE': current_site.name,
        'SEO_META_KEYWORDS': get_meta_keywords(),
        'SEO_META_DESCRIPTION': get_meta_description(),
    }
