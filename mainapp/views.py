# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from mainapp.forms import YoutubeForm , telegramForm , fresheyesForm , postForm, commentForm
from mainapp.models  import Youtube , telegram_model , fresheyes_post , post ,comment



def home(request):
    return render(request, "home.html")#response

#youtube functions

def youtube(request):
    biology =Youtube.objects.filter(Categorization='B')
    microbiology =Youtube.objects.filter(Categorization='M')
    physiology =Youtube.objects.filter(Categorization='P')

    return render(request, 'youtube.html', {'biology': biology,
                                             'microbiology':microbiology,
                                             'physiology':physiology})

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
                                             'microbiology':microbiology,
                                             'physiology':physiology})

def telegramfunction(request):

    if request.method == 'POST':
        telegram_Form = telegramForm(request.POST)
        if telegram_Form.is_valid():
            telegram_Form.save()
            return HttpResponseRedirect(reverse('mainapp:telegram'))

    elif request.method == 'GET':

        form = telegramForm()

    return render(request, "upload_telegram.html", {'form': form})

#Fresh eyes functions

def fresh_eyes (request):
    biology =fresheyes_post.objects.filter(Categorization='B')
    microbiology =fresheyes_post.objects.filter(Categorization='M')
    physiology =fresheyes_post.objects.filter(Categorization='P')

    return render(request, 'fresheyes.html', {'biology': biology,
                                             'microbiology':microbiology,
                                             'physiology':physiology})

def fresheyesfunction (request):
    # if request.method == 'POST':
    #     fresheyes_Form = fresheyesForm(request.POST)
    #     if fresheyes_Form.is_valid():
    #         fresheyes_Form.save()
    #         return HttpResponseRedirect(reverse('mainapp:fresheyes'))
    # elif request.method == 'GET':
    #     form = fresheyesForm()
    #     return render(request, "upload_fresheyes.html", {'form': form})

    if request.method == 'POST':
        form = fresheyesForm(request.POST, request.FILES) #the diffrence here is the type of request
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:fresh_eyes'))
    else:
        form = fresheyesForm()
    return render(request, "upload_fresheyes.html", {'form': form})

#wrong way#

# def handle_uploaded_file(f):
#     filename = fresheyes_model.Title  # get the name here
#     destination = open('upload_fresheyes/'+filename, 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#     destination.close()


# def upload(request):
#     if request.method == 'POST':
#         handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
#         return HttpResponse("Successful")
#
#     return HttpResponse("Failed")
#
# def handle_uploaded_file(file, filename):
#     if not os.path.exists('upload/'):
#         os.mkdir('upload/')
#
#     with open('upload/' + filename, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)

#end of wrong way#

#study group functions

def study_group(request):

    biology =post.objects.filter(Categorization='B')
    microbiology =post.objects.filter(Categorization='M')
    physiology =post.objects.filter(Categorization='P')

    return render(request, 'studygroup.html', {'biology': biology,
                                             'microbiology':microbiology,
                                             'physiology':physiology})

def studygroup_postForm(request):
    if request.method == 'POST':
        post_Form = postForm(request.POST)
        if post_Form.is_valid():
            post_Form.save()
            return HttpResponseRedirect(reverse('mainapp:study_group'))

    elif request.method == 'GET':

        form = postForm()

    return render(request, "upload_post.html", {'form': form})

def studygroup_commentForm(request):
    if request.method == 'POST':
        comment_Form = commentForm(request.POST)
        if comment_Form.is_valid():
            comment_Form.save()
            return HttpResponseRedirect(reverse('mainapp:studygroup'))

    elif request.method == 'GET':

        form = commentForm()

    return render(request, "upload_comment.html", {'form': form})
