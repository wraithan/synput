from django.conf.urls.defaults import *

urlpatterns = patterns('synput.todolist.views',
        url(r'^projects/$', 'project_list', name='todolist-project-list'),
        url(r'^projects/create/$', 'project_create',
            name='todolist-project-create'),
        url(r'^tags/$', 'tag_list', name='todolist-tag-list'),
        url(r'^tags/create/$', 'tag_create', name='todolist-tag-create'),
        url(r'^tasks/create/$', 'task_create', name='todolist-task-create'),
)
