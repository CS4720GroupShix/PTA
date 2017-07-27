"""proj1 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from pta import views as pta_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'pta/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^signup/$', pta_views.signup, name='signup'),
    url(r'^abouttheteam/$', pta_views.meettheteam, name='meettheteam'),
    # url(r'^abouttheteam/$', pta_views.AboutTeamView.as_view(), name='meettheteam'),
    url(r'^$', pta_views.homepage, name='homepage'),
    url(r'^edituser$', pta_views.edituser, name='edituser'),
    #url(r'^$', TemplateView.as_view(template_name='pta/home.html'), name='homepage'),
    url(r'^pta/', include('pta.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^homework/$', pta_views.homework, name='homework'),
    url(r'^homework/add$', pta_views.addhomework, name='addhomework'),
    url(r'^todo/$', pta_views.todo, name='todo'),
    url(r'^wishlist/$', pta_views.wishlist, name='wishlist'),
    url(r'^wishlist/add$', pta_views.addwishlist, name='addwishlist'),
]