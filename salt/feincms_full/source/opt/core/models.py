# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django import forms
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel

import feincms_cleanse
from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.raw.models import RawContent
from feincms.content.image.models import ImageContent
from feincms.content.video.models import VideoContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.application.models import ApplicationContent
from feincms.content.contactform.models import ContactFormContent
from feincms.module.page.extensions.navigation import NavigationExtension, PagePretender
from feincms.content.application.models import app_reverse


#
# Page
#
# extensions are declared in the reverse order that they appear in the admin
Page.register_extensions(
    'feincms.module.extensions.changedate',
    'feincms.module.extensions.translations',
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.excerpt',
    'feincms.module.extensions.seo',
    'feincms.module.page.extensions.titles',
)
Page.register_templates(
    {
        'key': 'home',
        'title': 'Homepage Template',
        'path': 'home.html',
        'regions': (
            ('main', _('Main region')),
        )
    },
    {
        'key': '1col',
        'title': 'One Column Template',
        'path': '1col.html',
        'regions': (
            ('main', _('Main region')),
        )
    },
    {
        'key': '2col',
        'title': 'Two Column Template',
        'path': '2col.html',
        'regions': (
            ('main', _('Main region')),
            ('sidebar', _('Sidebar'), 'inherited'),
        )
    },
    {
        'key': 'blank',
        'title': 'Blank Template',
        'path': 'blank.html',
        'regions': (
            ('main', _('Main region')),
        )
    }
)
Page.create_content_type(RichTextContent)
Page.create_content_type(
    MediaFileContent,
    TYPE_CHOICES=(
        ('left', _('Float left')),
        ('right', _('Float right')),
        ('default', _('Default position')),
        ('sidebar', _('Sidebar')),
    )
)
Page.create_content_type(RawContent)
Page.create_content_type(ContactFormContent)
Page.create_content_type(VideoContent)


#
# gallery
#
from gallery.models import GalleryContent

Page.create_content_type(GalleryContent)


#
# elephantblog
#
from elephantblog.models import Entry

# extensions are declared in the reverse order that they appear in the admin
# NOTE: the 'seo' extension must be defined AFTER the 'translations' extension,
# otherwise it generates a django error
Entry.register_extensions(
    # 'feincms.extensions.featured',
    'feincms.module.extensions.changedate',
    # 'feincms.module.extensions.datepublisher',
    'feincms.module.extensions.translations',
    'feincms.module.page.extensions.excerpt',
    'feincms.module.extensions.seo',
    'feincms.module.page.extensions.titles',
    'elephantblog.extensions.blogping',
    'elephantblog.extensions.tags',
)
Entry.register_regions(
    ('main', _('Main region')),
)
Entry.create_content_type(
    RichTextContent,
    cleanse=feincms_cleanse.cleanse_html, 
    regions=('main',)
)
Entry.create_content_type(
    MediaFileContent, 
    TYPE_CHOICES=(
        ('left', _('Float left')),
        ('right', _('Float right')),
        ('default', _('Default position')),
    )
)
Entry.create_content_type(RawContent)
Entry.create_content_type(VideoContent)


#
# application content
#
Page.create_content_type(
    ApplicationContent, 
    APPLICATIONS=(
        ('elephantblog.urls', 'Blog'),
        ('haystack.urls', 'Search'),
    )
)
