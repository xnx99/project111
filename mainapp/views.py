# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "home.html")#response

#def youtube(request):
        #return render(request, "youtube.html")#response
def youtube(request):
     #try:
         #youtube = Youtube.objects.get(pk= video_uploadedby_id)
     #except Youtube.DoesNotExist:
         #raise Http404('Sorry, this page does not exist.')
     #return render(request, "youtube.html")

    youtube = get_object_or_404
    return render(request, 'youtube.html', {'youtube': youtube})

def uploade_video(request, video_uploadedby_id):
    Video_Title = request.POST['Title']
    Video_Description = request.POST['Description']
    Video_Categorization = request.POST['Categorization']
    youtube = get_object_or_404

    Youtube.objects.create(Video_Title=Video_Title, Video_Description=Video_Description, Video_Categorization=Video_Categorization)
    redirect_url = reverse('mainapp:uploade_video', args=[video_uploadedby_id])
    return HttpResponseRedirect(redirect_url)


