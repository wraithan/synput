from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^todolist/', include('synput.todolist.urls')),
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^accounts/profile/$', direct_to_template, {
            'template': 'profile.html'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': '/home/wraithan/devel/synput/media/'}),
)
