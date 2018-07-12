# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
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

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:studygroup'))

    elif request.method == 'GET':

        form = commentForm()

    context={'biology':biology,
             'microbiology':microbiology,
             'physiology':physiology}

    context['form']=form
    return render(request, 'studygroup.html',context)

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

#trying to be cool
def list_posts(request,pk, selector=None):
    # category = post.objects.get_from_slugs_or_404(slugs)
    post = get_object_or_404(post, pk=pk)
    #exam = get_object_or_404(Exam.objects.select_related('category'), pk=pk, category=category)
    post_pk= get_object_or_404(post.objects.select_related('post'), pk=pk, post=post)
    # assignment_form = forms.AssignQuestionForm(exam=exam) << i do not know how to apply it
    # # PERMISSION CHECK
    # if not exam.can_user_access(request.user):
    #     raise PermissionDenied

    context = {'Issue': Issue,
               'selector':selector
               #form is missing
               #is deleted button is missing
               }

    if selector:
        if selector.startswith('i-'):
            issue_pk = int(selector[2:])
            issue = get_object_or_404(Issue, pk=issue_pk)
            context['list_name'] = issue.name #what is list name?
            elif selector.startswith('s-'):
                pk_post = int(selector[2:])
                subject = get_object_or_404(post_pk.subject_set, pk=pk_post)
                context['list_name'] = subject.name #what is list name?
            if selector == 'all':
                context['all'] = post_pk.objects.all
            elif selector == 'biology':
                context['biology']=post_pk.objects.filter(Categorization='B')
            elif selector == 'microbiology':
                context['microbiology']=post_pk.objects.filter(Categorization='M')
            elif selector == 'physiology':
                context['physiology']=post_pk.objects.filter(Categorization='P')
            else:
                raise Http404
            return render(request, 'studygroup.html', context)
        else: #if no selector
            context['issues'] = Issue.objects.all()
            return render(request, 'studygroup.html', context)
