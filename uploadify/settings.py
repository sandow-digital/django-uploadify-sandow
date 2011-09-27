from django.conf import settings
STATIC_URL = getattr(settings, 'STATIC_URL', '')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '')


# Uploadify root folder path, relative to MEDIA_ROOT
UPLOADIFY_PATH = '%s%s' % (STATIC_URL, 'common/js/uploadify/')


UPLOADIFY_UPLOAD_PATH = '%s%s' % (MEDIA_URL, 'photos/')
