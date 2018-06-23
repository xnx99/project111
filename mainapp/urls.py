from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'youtube/',views.youtube , name='youtube'),
    url(r'upload_video/',views.Youtubefunction , name='upload_video'),
    url(r'upload_telegram/',views.telegramfunction , name='upload_telegram'),
    url(r'telegram/',views.telegram_biology, name='biology'),
    url(r'telegram/',views.telegram_microbiology, name='microbiology'),
    url(r'telegram/',views.telegram_physiology, name='physiology'),

]
