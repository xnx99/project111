# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Youtube(models.Model):
    Video_Title=models.TextField(max_length=500)
    video_uploadedby=models.ForeignKey
    Video_Description=models.TextField(max_length=500)
    Video_Categorization=models.CharField(max_length=30)
    Video_Date= models.DateTimeField('date published',auto_now_add=True)
    video_is_deleted= models.BooleanField(verbose_name="هل الفديو محذوف؟",default=False)



