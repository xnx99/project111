# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse



Categorization_choices = (
    ('','--'),
    ('B', u'biology'),
    ('M', u'microbiology'),
    ('P', u'physiology'),
)

#youtube model

class Youtube(models.Model):
    Title=models.TextField(max_length=75)
    uploadedby=models.ForeignKey(User ,null=True)
    Description=models.TextField(max_length=150)
    Categorization=models.CharField(max_length=1, choices=Categorization_choices)
    Date= models.DateTimeField('date published',auto_now_add=True)
    is_deleted= models.BooleanField(verbose_name="هل الفديو محذوف؟",default=False)
    link=models.TextField(max_length=100)

#telegram model

class telegram_model(models.Model):
    Title=models.TextField(max_length=75)
    uploadedby=models.ForeignKey(User ,null=True)
    Description=models.TextField(max_length=150)
    Categorization=models.CharField(max_length=1, choices=Categorization_choices)
    Date= models.DateTimeField('date published',auto_now_add=True)
    is_deleted= models.BooleanField(verbose_name="هل القناة محذوف؟",default=False)
    link=models.TextField(max_length=100)

#Fresh eyes model

class fresheyes_model(models.Model):
    Title=models.TextField(max_length=75)
    uploadedby=models.ForeignKey(User ,null=True)
    Description=models.TextField(max_length=150)
    Categorization=models.CharField(max_length=1, choices=Categorization_choices)
    Date= models.DateTimeField('date published',auto_now_add=True)
    is_deleted= models.BooleanField(verbose_name="هل المستند محذوف؟",default=False)
    file= models.FileField()


    def __unicode__(self):
        return unicode(self.file) or u''



# study group

class Article(models.Model):
    author = models.CharField(max_length=80)
    title = models.CharField(max_length=200, default='First Title')
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('تاريخ النشر',auto_now_add=True)
    is_deleted= models.BooleanField(verbose_name="هل الموضوع محذوف؟",default=False)

    class Meta:
        verbose_name='مقالة'
        verbose_name_plural='مقالات'

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article)
    author = models.CharField(max_length=80)
    text = models.TextField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
