from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$' , views.home , name='home'),
    url(r'youtube/',views.youtube , name='youtube'),

]
