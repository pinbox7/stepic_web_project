from django.conf.urls import url
#from qa.views import test

urlpatterns = [
    url(r'^$', 'test'),
    url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),
    url(r'^popular/.*', 'test', name='popular'),
    url(r'^ask/.*', 'test', name='ask'),
    url(r'^signup/.*', 'test', name='signup'),
    url(r'^login/.*$', 'test', name='login'),
    url(r'^new/.*', 'test', name='new'),
]
