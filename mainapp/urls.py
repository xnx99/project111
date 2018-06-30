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

]
