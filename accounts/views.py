# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from userena.utils import signin_redirect

from django.shortcuts import render

from userena import views as userena_views
from django.http import HttpResponseRedirect, Http404, HttpResponse
from userena.utils import signin_redirect
from django.contrib.auth import REDIRECT_FIELD_NAME

