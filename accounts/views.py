# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from userena import views as userena_views

# Create your views here.

def signup(request):
    return userena_views.signup(request, template_name='accounts/signup.html')
