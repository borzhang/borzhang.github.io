#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'borzhang'
SITENAME = u'zuomo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

DEFAULT_DATE = 'fs'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}

THEME = "../pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
	'summary', 
	'render_math',
	'tag_cloud',
	'i18n_subsites',
]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Scikit-learn', 'http://scikit-learn.org/stable/index.html'),
#          ('Python.org', 'http://python.org/'),
#          )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = False
TAG_CLOUD_STEPS = 3

DISPLAY_ARTICLE_INFO_ON_INDEX = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
