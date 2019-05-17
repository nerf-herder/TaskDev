# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class BaseModel(models.Model):
    '''
        This is going to be the new base model
        The django auto_now and auto_now_add do not operate as expected.
        They tend to give inaccurate results for date this abstract model addresses that issue.
    '''
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Task(BaseModel):
    CATEGORIES = (
        ('0', 'Urgent & Important'),
        ('1', 'Urgent'),
        ('2', 'Important'),
        ('3', 'Other'),
    )

    name = models.CharField(max_length=500, default='To-Do Label')
    quad = models.IntegerField(default=0)
    category = models.CharField(max_length=100, default=CATEGORIES[0][0], choices=CATEGORIES)
    completed = models.BooleanField(default=False)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return "tasks: {}".format(self.name)

    class Meta:
        ordering = ['quad', 'category', 'ordering']
