from django.conf.urls.defaults import *

urlpatterns = patterns('synput.todolist.views',
        url(r'^projects/$', 'project_list', name='todolist-project-list'),
        url(r'^projects/create/$', 'project_create',
            name='todolist-project-create'))
