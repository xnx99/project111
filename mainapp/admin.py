# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Youtube, telegram_model ,fresheyes_post ,post

#registering
admin.site.register(Youtube)
admin.site.register(telegram_model)
admin.site.register(fresheyes_post)
admin.site.register(post)
