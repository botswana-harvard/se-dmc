from django.db import models


class Project(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    duration = models.DecimalField(verbose_name='Project duration')
    active = models.BooleanField(defaut=False, verbose_name='Is project ative')