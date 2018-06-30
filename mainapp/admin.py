# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import Youtube, telegram_model


admin.site.register(Youtube)
admin.site.register(telegram_model)
