from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from synput.todolist.models import Project, Tag
from synput.todolist.forms import ProjectForm, TagForm


@login_required
def project_list(request):
    title = 'List of projects'
    projects = Project.objects.filter(user=request.user)
    return render_to_response('todolist/projects.html', {
        'title': title,
        'list_of_projects': projects},
        context_instance=RequestContext(request))


@login_required
def project_create(request):
    title = 'Create new project'
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            return HttpResponseRedirect(reverse('todolist-project-list'))
    else:
        form = ProjectForm()
    # Purposely outside of the else, this way if the form is not valid it is
    # rendered with errors set so the user can correct them.
    return render_to_response('todolist/project_form.html', {
            'title': title,
            'form': form},
            context_instance=RequestContext(request))


@login_required
def tag_list(request):
    title = 'List of tags'
    tags = Tag.objects.filter(user=request.user)
    return render_to_response('todolist/tags.html', {
        'title': title,
        'list_of_tags': tags},
        context_instance=RequestContext(request))


@login_required
def tag_create(request):
    title = 'Create new tag'
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            return HttpResponseRedirect(reverse('todolist-tag-list'))
    else:
        form = TagForm()
    # Purposely outside of the else, this way if the form is not valid it is
    # rendered with errors set so the user can correct them.
    return render_to_response('todolist/tag_form.html', {
            'title': title,
            'form': form},
            context_instance=RequestContext(request))
