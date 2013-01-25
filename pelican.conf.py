#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Alan Briolat"
SITENAME = u"Digital Ambulation"
SITEURL = u'http://alanbriolat.co.uk'

TIMEZONE = 'Europe/London'

DEFAULT_LANG='en'

PLUGINS = ['pelican.plugins.assets']

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    ('You can modify those links in your config file', '#')
         )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

DEFAULT_PAGINATION = 10

ARTICLE_DIR = 'articles'
PAGE_DIR = 'pages'
STATIC_PATHS = ['images', 'downloads']

# This scheme matches my old Wordpress setup
DEFAULT_CATEGORY = 'uncategorized'
#ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
#ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
#TAG_URL = 'tag/{name}/'
#TAG_SAVE_AS = 'tag/{name}/index.html'
#CATEGORY_URL = 'category/{name}/'
#CATEGORY_SAVE_AS = 'category/{name}/index.html'

THEME = 'themes/digitalambulation'
THEME_STATIC_PATHS = ['static']

FEED_DOMAIN = SITEURL

DISQUS_SITENAME = "digitalambulation"
GOOGLE_ANALYTICS = "UA-12964289-1"
