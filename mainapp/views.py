# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from mainapp.forms import YoutubeForm , telegramForm , fresheyesForm , postForm, commentForm
from mainapp.models  import Youtube , telegram_model , fresheyes_post , comment , post
from django.contrib.auth.decorators import login_required
import random
import os
import posixpath
from django import template
from django.conf import settings
from django.utils import timezone
from django.views.decorators import csrf
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST, require_safe
from mainapp import decorators

def home(request):
     return render(request, "home.html")#response:

def authentication(request):
    # return render(request, "home.html")#response:
    if request.user.is_authenticated():
        return render(request, 'index_authenticated.html')

    else:
        return render(request, 'home.html')


#youtube functions
def youtube(request):
    biology =Youtube.objects.filter(Categorization='B' , is_deleted='False')
    microbiology =Youtube.objects.filter(Categorization='M' , is_deleted='False')
    physiology =Youtube.objects.filter(Categorization='P', is_deleted='False')

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

    biology =telegram_model.objects.filter(Categorization='B', is_deleted='False')
    microbiology =telegram_model.objects.filter(Categorization='M',is_deleted='False')
    physiology =telegram_model.objects.filter(Categorization='P',is_deleted='False')

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
def upload_fresheyes (request):
    if request.method == 'POST':
        form = fresheyesForm(request.POST, request.FILES) #the diffrence here is the type of request
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:fresheyes'))
    else:
        form = fresheyesForm()
    return render(request, "upload_fresheyes.html", {'form': form})

def upload_comment(request):
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:fresheyes'))

    elif request.method == 'GET':

        form = commentForm()
    return {}

def fresheyes (request,selector=None):
    context = {}
    problem = fresheyes_post.objects.filter(is_deleted= False)

    if selector:
        if selector == 'biology':
            context['problem'] = problem.filter(Categorization='B')
            context['problem_type'] = "Biology"
        elif selector == 'microbiology':
            context['problem'] = problem.filter(Categorization='M')
            context['problem_type'] = "microbiology"
        elif selector == 'physiology':
            context['problem'] = problem.filter(Categorization='P')
            context['problem_type'] = "physiology"
        else:
            raise Http404
        return render(request, 'fresheyes.html', context)
    else:
        context['problem'] = problem
        context['problem_type'] = "All"
    return render(request, "fresheyes.html", context)


#study group functions
def studygroup_postForm(request):
    if request.method == 'POST':
        instance = post(uploadedby = request.user)
        Form = postForm(request.POST, request.FILES, instance=instance)
        if Form.is_valid():
            Form.save()
            return HttpResponseRedirect(reverse('mainapp:list_posts'))
    elif request.method == 'GET':
        form = postForm()
    return render(request, "upload_post.html", {'form': form})

def studygroup_commentForm(request):
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:list_posts'))

    elif request.method == 'GET':

        form = commentForm()
    return {}
def list_posts(request,selector=None):
    context = {}
    posts = post.objects.filter(is_deleted= False)

    if selector:
        if selector == 'biology':
            context['list'] = posts.filter(Categorization='B')
            context['list_name'] = "Biology"
        elif selector == 'microbiology':
            context['list'] = posts.filter(Categorization='M')
            context['list_name'] = "microbiology"
        elif selector == 'physiology':
            context['list'] = posts.filter(Categorization='P')
            context['list_name'] = "physiology"
        else:
            raise Http404
        return render(request, 'studygroup_new.html', context)
    else:
        context['list'] = posts
        context['list_name'] = "All"
    return render(request, "studygroup_new.html", context)

def show_post(request,pk):
    article = get_object_or_404(post,pk=pk)
    comment1 = comment.objects.all()
    context= {'article':article,
              'comment1':comment1
     }
    if request.method == 'POST':
        instance = comment(post=article,uploadedby=request.user)
        form = commentForm(request.POST, instance=instance)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect(
                reverse("mainapp:show_post",
                        args=(pk)))

    elif request.method == 'GET':
        form = commentForm()
    context['form']= form

    return render(request, 'studygroup_post.html',context)

# def reply_to_comment(request,pk ,commentid):
#
#     reply=replyForm.object.filter(parent='parent'
#                                   ,commentid=commentid)
#     context= {'reply':reply}
#     if request.method == 'POST':
#         reply_form = replyForm(request.POST)
#         if reply_form.is_valid():
#              reply_form.save()
#              return HttpResponseRedirect(
#                 reverse("mainapp:show_post",
#                         args=(pk,commentid)
#                         ))
#
#     elif request.method == 'GET':
#         form = replyForm()
#     context['form']= form
#
#     return render(request, 'studygroup_post.html',context)
# -
# register = template.Library()
#
# @register.simple_tag
# def random_image():
#     list_images = os.listdir(path=settings.RANDOM_IMAGES)
#     return random.choice(list_images)
# @login_required do not forget to use it @_@
#-
def reply_comment(request):
    article = get_object_or_404(post,)
    if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	#share_string = quote_plus(instance.content)
    initial_data = {
    "content_type": instance.get_content_type,
    "object_id": instance.id
    }

    form = commentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		# content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = comment.objects.get_or_create(
							user = request.user,
							# content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	# comments = instance.comments
    context = {
    # "title": instance.title,
    # "instance": instance,
    # "share_string": share_string,
    # "comments": comments,
    "post":post,
    "comment_form":form,
}

    return render(request, "studygroup_post.html", context)

@require_POST
@csrf.csrf_exempt
@decorators.ajax_only
def delete_article(request, pk):
    article = get_object_or_404(post, pk=pk)
        # PERMISSION CHECK
    if not request.user.is_superuser and \
       not article.uploadedby == request.user :
        raise Exception("You cannot delete that question!")


    article.is_deleted = True
    article.save()

    return  {"message": "success"}


@require_POST
@csrf.csrf_exempt
@decorators.ajax_only
def delete_video(request, pk):
    video = get_object_or_404(Youtube, pk=pk)
        # PERMISSION CHECK
    if not request.user.is_superuser and \
       not video.uploadedby == request.user :
        raise Exception("You cannot delete this video!")


    video.is_deleted = True
    video.save()

    return  {"message": "success"}

@require_POST
@csrf.csrf_exempt
@decorators.ajax_only
def delete_channel(request, pk):
    channel = get_object_or_404(telegram_model, pk=pk)
        # PERMISSION CHECK
    if not request.user.is_superuser and \
       not channel.uploadedby == request.user :
        raise Exception("You cannot delete this channel!")


    channel.is_deleted = True
    channel.save()

    return  {"message": "success"}
