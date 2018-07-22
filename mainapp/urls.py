from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'studygroup/(?P<selector>[\-\d\w_]+)/$', views.list_posts, name='list_posts'),
    url(r'studygroup/$', views.list_posts, name='list_posts'),
    url(r'youtube/',views.youtube , name='youtube'),
    url(r'upload_video/',views.Youtubefunction , name='upload_video'),
    url(r'upload_telegram/',views.telegramfunction , name='upload_telegram'),
    url(r'telegram/',views.telegram, name='telegram'),
    url(r'upload_fresheyes/',views.fresheyesfunction , name='upload_fresheyes'),
    url(r'fresh_eyes/',views.fresh_eyes, name='fresh_eyes'),
    url(r'studygroup/posts/(?P<pk>\d+)/$', views.show_post, name='show_post'),
    # url(r'studygroup/(?P<pk>\d+)/(?P<comment_id >\d+)//$', views.reply_to_comment , name='replies'),
    url(r'upload_post/',views.studygroup_postForm , name='upload_post'),
    # url(r'upload_comment/',views.studygroup_commentForm , name='upload_comment'),
    # url(r'study_group/',views.study_group, name='study_group'),
    # url(r'(?P<pk>\d+)/studygroup/(?P<selector>[\-\d\w_]+)/$', views.list_posts, name='list_posts_by_selector'),
    #AJAX
    url(r'^ajax/delete/(?P<pk>\d+)$', views.delete_article, name='delete_article'),
    url(r'^ajax/video/delete/(?P<pk>\d+)$', views.delete_video, name='delete_video'),
]
