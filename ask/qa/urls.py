from django.conf.urls import url
# from . import views
from qa.views import test, q_list, question_detail, popular


urlpatterns = [
    url(r'^$', q_list, name='q_list'),
    url(r'^question/(?P<id>d+)/$', question_detail, name='question_detail'),
    url(r'^popular/.*', popular, name='popular'),
    url(r'^ask/.*', test, name='ask'),
    url(r'^signup/.*', test, name='signup'),
    url(r'^login/.*$', test, name='login'),
    url(r'^new/.*', test, name='new'),
]
