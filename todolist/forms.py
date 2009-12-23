from django.forms import ModelForm

from synput.todolist.models import Project, Tag, Task


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name']


class TagForm(ModelForm):

    class Meta:
        model = Tag
        fields = ['name']


class TaskForm(ModelForm):

    class Meta:
        model = Task
