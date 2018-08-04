from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'studygroup/(?P<selector>[\-\d\w_]+)/$', views.list_posts, name='list_posts'),
    url(r'studygroup/$', views.list_posts, name='list_posts'),
    url(r'studygroup/posts/(?P<pk>\d+)/$', views.show_post, name='show_post'),
    url(r'upload_post/',views.studygroup_postForm , name='upload_post'),
    url(r'upload_video/',views.Youtubefunction , name='upload_video'),
    url(r'upload_telegram/',views.telegramfunction , name='upload_telegram'),
    url(r'upload_fresheyes/',views.upload_fresheyes , name='upload_fresheyes'),
    url(r'telegram/',views.telegram, name='telegram'),
    url(r'youtube/',views.youtube , name='youtube'),
    url(r'fresheyes/(?P<selector>[\-\d\w_]+)/$', views.fresheyes, name='fresheyes'),
    url(r'fresheyes/$', views.fresheyes, name='fresheyes'),

    # url(r'upload_comment/',views.studygroup_commentForm , name='upload_comment'),
    #AJAX
    url(r'^ajax/delete/(?P<pk>\d+)$', views.delete_article, name='delete_article'),
    url(r'^ajax/video/delete/(?P<pk>\d+)$', views.delete_video, name='delete_video'),
    url(r'^ajax/channel/delete/(?P<pk>\d+)$', views.delete_channel, name='delete_channel'),

]

