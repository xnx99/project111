"""project111 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from mainapp.views import home
from userena import views as userena_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mainapp/', include('mainapp.urls', namespace="mainapp")),
    url(r'^$',home,name='home' ),
    url(r'^accounts/', include('userena.urls')),
    url(r'^signup/$',userena_views.signup,name='userena_signup'),
    url(r'^signin/$',userena_views.signin,name='userena_signin'),
    url(r'^signout/$',userena_views.signout,name='userena_signout'),

]
