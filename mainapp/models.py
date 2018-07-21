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

class fresheyes_post(models.Model):
    Title=models.TextField(max_length=75)
    uploadedby=models.ForeignKey(User ,null=True)
    help_type=models.TextField(max_length=150,default=True,verbose_name=u"نوع المساعدة؟")
    Categorization=models.CharField(max_length=1, choices=Categorization_choices)
    Date= models.DateTimeField('date published',auto_now_add=True)
    is_deleted= models.BooleanField(verbose_name="هل المستند محذوف؟",default=False)
    file= models.FileField(upload_to='Fresh_eyes/', null=True, blank=True)


    def __unicode__(self):
        return unicode(self.file) or u''


class fresheyes_comment(models.Model):
    post=models.ForeignKey(fresheyes_post)
    text=models.TextField(max_length=150)
    is_deleted= models.BooleanField(verbose_name="هل المستند محذوف؟",default=False)
    file= models.FileField(upload_to='Fresh_eyes/comment/', null=True, blank=True)


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
    uploadedby=models.ForeignKey(User ,null=True)
    Description=models.TextField(max_length=150)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    Categorization=models.CharField(max_length=1, choices=Categorization_choices)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    is_deleted= models.BooleanField(verbose_name="هل المقال محذوف؟",default=False)


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

    def get_absolute_url(self):
        return reverse("posts:detail")

class comment(models.Model):
    """
    A comment on a news post.
    """
    post = models.ForeignKey(post)
    uploadedby=models.ForeignKey(User ,null=True)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies')
    is_deleted= models.BooleanField(verbose_name="هل التعليق محذوف؟",default=False)

    def __unicode__(self):
        return "Comment by %s on post '%s'" % (self.author, self.post.title)

    def children(self): #replies
         return comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

#for issue selector

# class Issue(models.Model):
#     name = models.CharField(max_length=100)
#     # code_name is something more stable than 'name'
#     code_name = models.CharField(max_length=50)
#     is_blocker = models.BooleanField(default=False)
#
#     def get_selector(self):
#         return 'i-' + str(self.pk)
#
#     def __str__(self):
#         if self.is_blocker:
#             blocker_str = "blocker"
#         else:
#             blocker_str = "non-blocker"
#
#         return "{} ({})".format(self.name, blocker_str)
