# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class CommonProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                             unique=True,
                             verbose_name=_('user'),
                             related_name='common_profile')
    ar_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    ar_middle_name = models.CharField(max_length=30,
                                      verbose_name=u'الاسم الأوسط')
    ar_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    en_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    en_middle_name = models.CharField(max_length=30,
                                      verbose_name=u'الاسم الأوسط')
    en_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    alternative_email = models.EmailField(u"البريد الإلكتروني  الشخصي البديل",
                                          blank=True)
    mobile_number = models.CharField(max_length=20, blank=True,
                                     verbose_name=u'رقم الجوال')

    def get_ar_full_name(self):
        ar_fullname = None
        try:
            # If the Arabic first name is missing, let's assume the
            # rest is also missing.
            if self.ar_first_name:
                ar_fullname = " ".join([self.ar_first_name,
                                     self.ar_middle_name,
                                     self.ar_last_name])
        except AttributeError: # If the user has their details missing
            pass

        return ar_fullname

    def get_en_full_name(self):
        en_fullname = None
        try:
            # If the English first name is missing, let's assume the
            # rest is also missing.
            if self.en_first_name:
                en_fullname = " ".join([self.en_first_name,
                                     self.en_middle_name,
                                     self.en_last_name])
        except AttributeError: # If the user has their details missing
            pass

        return en_fullname





