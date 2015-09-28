#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'webmaster'
SITENAME = u'Website'
SITEURL = u'http://localhost:8000'
TIMEZONE = u'Europe/Zurich'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a %d. %B %Y'

# Page path
PAGE_PATHS = ['pages']
DIRECT_TEMPLATES = ['categories', 'authors', 'tags', 'archives']
PAGINATED_DIRECT_TEMPLATES = []

# Pagination
DEFAULT_PAGINATION = 10
# Have at least 2 articles on the last page
DEFAULT_ORPHANS = 2

# Menu
MENUITEMS = (   ('Pages', '#', [
                    ('Page1', '/page1.html'),
                    ('Page2', '/page2.html'),
                ]),
                ('Tags', '/tags/index.html', None),
                ('Categories', '/category/index.html', None),
                ('Authors', '/author/index.html', None),
                ('Archives', '/archives.html', None),)

# don't show categories and pages in the menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
FEED_RSS = 'feeds/rss.xml'
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL settings
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_SAVE_AS = 'author/index.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORIES_SAVE_AS = 'category/index.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_URL = '{category}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags/index.html'
TAGS_SAVE_AS = 'tags/index.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

# Contact
EMAIL_ADDR = 'webmaster@example.net'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Theme
THEME = 'theme'
STATIC_PATHS = ['images', 'docs', 'extra/robots.txt', 'extra/favicon.ico']
PATH_METADATA = 'pages/(?P<path>.*)\..*'
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Licence
LICENCE_NAME = 'BY-NC-SA'
LICENCE_URL = 'http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US'
LICENCE_URL_IMG = 'http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png'
