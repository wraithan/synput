from django.forms import ModelForm, ModelMultipleChoiceField, ModelChoiceField

from synput.todolist.models import Project, Tag, Task


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ['user']


class TagForm(ModelForm):

    class Meta:
        model = Tag
        exclude = ['user']


class TaskForm(ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(user=user)
            self.fields['tags'].queryset = Tag.objects.filter(user=user)

    class Meta:
        model = Task
