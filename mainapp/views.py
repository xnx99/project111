# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from mainapp.forms import YoutubeForm , telegramForm
from mainapp.models  import Youtube , telegram_model



def home(request):
    return render(request, "home.html")#response

#youtube function

def youtube(request):

    youtube_videos = Youtube.objects.all()
    youtube = get_object_or_404
    return render(request, 'youtube.html', {'youtube_videos': youtube_videos})

#youtube form function

def Youtubefunction(request):

    if request.method == 'POST':
        Youtube_Form = YoutubeForm(request.POST)
        if Youtube_Form.is_valid():
            Youtube_Form.save()
            return HttpResponseRedirect(reverse('mainapp:youtube'))

    elif request.method == 'GET':

        form = YoutubeForm()

    return render(request, "upload_video.html", {'form': form})


#telegram functions

def telegram(request):

    biology =telegram_model.objects.filter(Categorization='B')
    microbiology =telegram_model.objects.filter(Categorization='M')
    physiology =telegram_model.objects.filter(Categorization='P')

    return render(request, 'telegram.html', {'biology': biology,
                                             'microbiology':microbiology ,
                                             'physiology':physiology})

#telegram = get_object_or_404
#telegram form function

def telegramfunction(request):

    if request.method == 'POST':
        telegram_Form = telegramForm(request.POST)
        if telegram_Form.is_valid():
            telegram_Form.save()
            return HttpResponseRedirect(reverse('mainapp:telegram'))

    elif request.method == 'GET':

        form = telegramForm()

    return render(request, "upload_telegram.html", {'form': form})
