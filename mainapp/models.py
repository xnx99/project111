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

#Fresh eyes models

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

# i did not make migrations because i'm still thinking how can i connect them by the ForeignKey
class fresheyes2_model(models.Model):
    Title=models.TextField(max_length=75)
    Description=models.TextField(max_length=150)
    is_deleted= models.BooleanField(verbose_name="هل المستند محذوف؟",default=False)
    file= models.FileField()


    def __unicode__(self):
        return unicode(self.file) or u''



# study group models

    # class Meta:
    #     verbose_name='مقالة'
    #     verbose_name_plural='مقالات'

class post(models.Model):
    """
    A news post.
    """
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")

    def has_image(self):
        return self.image != ""

    has_image.boolean = True
    has_image.short_description = "Has Image?"

    def get_summary(self):
        summary = self.body[:200]
        if len(self.body) > 200:
            summary += "..."
        return summary

    def __unicode__(self):
        return self.title


class comment(models.Model):
    """
    A comment on a news post.
    """
    post = models.ForeignKey(post)
    author = models.CharField(max_length=128)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Comment by %s on post '%s'" % (self.author, self.post.title)
