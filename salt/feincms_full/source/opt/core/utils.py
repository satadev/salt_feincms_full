# -*- coding: utf-8 -*-
from feincms.module.page.models import Page


def get_meta_description():
    """
    get meta description for homepage
    """
    try:
        page = Page.objects.get(override_url='/')
        return page.meta_description

    except Page.DoesNotExist:
        return ''

    except AttributeError:
        return ''


def get_meta_keywords():
    """
    get meta keywords for homepage
    """
    try:
        page = Page.objects.get(override_url='/')
        return page.meta_keywords

    except Page.DoesNotExist:
        return ''

    except AttributeError:
        return ''
