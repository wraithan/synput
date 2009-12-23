from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^todolist/', include('synput.todolist.urls')),
    (r'^$', direct_to_template, {'template': 'index.html'}),

    # Following are placeholders for when django-profile is setup:
    (r'^accounts/profile/$', direct_to_template, {
            'template': 'profile.html'}),
)
