from django.conf.urls import url
from qa.views import test, q_list, question_detail, popular
from qa.views import question_ask, question_answer


urlpatterns = [
    url(r'^$', q_list, name='q_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/', test, name='signup'),
    url(r'^login/$', test, name='login'),
    url(r'^logout/', test, name='logout'),
    url(r'^new/', test, name='new'),
]
