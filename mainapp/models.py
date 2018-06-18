# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse


# Create your models here.

Categorization_choices = (
    ('B', u'biology'),
    ('M', u'microbiology')
)

class Youtube(models.Model):
    Title=models.TextField(max_length=500)
    uploadedby=models.ForeignKey(User)
    Description=models.TextField(max_length=500)
    Categorization=models.CharField(max_length=1, choices=Categorization_choices)
    #Date= models.DateTimeField('date published',auto_now_add=True)
    is_deleted= models.BooleanField(verbose_name="هل الفديو محذوف؟",default=False)



