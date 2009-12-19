from synput.main.models import Project, Task, Tag
from django.contrib import admin


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)
admin.site.register(Tag)
