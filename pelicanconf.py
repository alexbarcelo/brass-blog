#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Beta & Rho'
SITENAME = 'BRASS Blog'
SITESURNAME = 'Sooomething else yadda yadda'
SITEURL = ''
MAIN_IMAGE = 'theme/clean-blog/img/home-bg.jpg'
DEFAULT_ARTICLE_IMAGE = 'theme/clean-blog/img/post-bg.jpg'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
ICONS = (('smile-beam', '#'),)
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
