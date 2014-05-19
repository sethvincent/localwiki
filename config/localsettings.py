DEBUG = False

#######################################################################
# Config values you *must* change
#######################################################################

ALLOWED_HOSTS = ['.{{ public_hostname }}', '127.0.0.1', '.localhost']

SESSION_COOKIE_DOMAIN = '.{{ public_hostname }}'
if SESSION_COOKIE_DOMAIN == '.localhost':
    SESSION_COOKIE_DOMAIN = None

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'localwiki',
        'USER': 'localwiki',
        'PASSWORD': '{{ postgres_db_pass }}',
        'HOST': '127.0.0.1',
    }
}

# For testing, you can start the python debugging smtp server like so:
# sudo python -m smtpd -n -c DebuggingServer localhost:25
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'dontreply@{{ public_hostname }}'

#######################################################################
# Other config values.
#######################################################################

OLWIDGET_CUSTOM_LAYER_TYPES = {
    'mblw': """OpenLayers.Layer.XYZ('MB LW',
        ["http://a.tiles.mapbox.com/v3/philipn.hjmo8m80/${z}/${x}/${y}.png"], {
            sphericalMercator: true,
            wrapDateLine: true,
    })""",
}

DAISYDIFF_URL = 'http://localhost:8080/daisydiff/diff'
DAISYDIFF_MERGE_URL = 'http://localhost:8080/daisydiff/merge'

# list of regular expressions for white listing embedded URLs
EMBED_ALLOWED_SRC = ['.*']

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://localhost:8080/solr/',
    }
}

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

LOCAL_INSTALLED_APPS = (
)

POSTGIS_VERSION = (2, 0, 3)

# cache settings
CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'KEY_PREFIX': '',
	    'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60,
    }
}

SECRET_KEY = '{{ django_secret_key }}'

SENTRY_REMOTE_URL = 'https://errors.localwiki.org/sentry/store/'
SENTRY_KEY = '{{ sentry_key }}'
