# THIS is not the way drew wants the views to be done. He wants functional views
# because too much information is abstracted from the view via generic views
# It is plausible to do that in some instances, however it is not that serious....
#
#
#from django.conf.urls import patterns, url
#
#from polls import views
#
#urlpatterns = patterns('',
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
#)


# doing views the functional way like below
from django.conf.urls import patterns, url
# from mysite.settings import STATIC_ROOT
from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

   # this url needs too be on the root not here in the apps urls.py
   # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT})


)