from django.conf.urls import patterns, include, url

# import our settings file to serve static assets
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from polls.api import PollResource

poll_resource = PollResource()
# this is where the main site hands off the users request to different apps should you have them
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #hands off the request to the polls app
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^api',include(poll_resource.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # url to match djangos requests for assets (js, css, img) and return them
    # change settings.Dev.... to STATIC_ROOT for production deployment (remember to run collectstatic too)
    # collectstatic pulls static files i.e. js and css and html( files that change often)
    # to the django files (files or infrastructure that will never change or rarely does)
    # so django can put them together to make the awesomeness that is a web page
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)