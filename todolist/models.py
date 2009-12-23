from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField('Project Name', max_length=50)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.name