from django.conf.urls import patterns, include, url
from invites.views import *

urlpatterns = patterns('',
	url(r'^$', landing),
)
