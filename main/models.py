from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)
    tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return self.name

