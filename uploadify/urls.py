from django.conf.urls import *
from uploadify.views import *

urlpatterns = [
    url(r'upload/$', upload, name='uploadify_upload'),
]
