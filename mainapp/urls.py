from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'youtube/',views.youtube , name='youtube'),
    url(r'upload_video/',views.Youtubefunction , name='upload_video'),
    url(r'upload_telegram/',views.telegramfunction , name='upload_telegram'),
    url(r'telegram/',views.telegram, name='telegram'),
    url(r'upload_fresheyes/',views.fresheyesfunction , name='upload_fresheyes'),
    url(r'fresh_eyes/',views.fresh_eyes, name='fresh_eyes'),
    # url(r'upload_post/',views.studygroup_postForm , name='upload_post'),
    # url(r'upload_comment/',views.studygroup_commentForm , name='upload_comment'),
    # url(r'study_group/',views.study_group, name='study_group'),
    url(r'(?P<pk>\d+)/studygroup/(?P<selector>[\-\d\w_]+)/$', views.list_posts, name='list_posts_by_selector'),
    url(r'(?P<pk>\d+)/studygroup/(?P<selector>[\-\d\w_]+)/$', views.list_posts, name='list_posts_by_selector'),
]
# i do not know which one is right?
