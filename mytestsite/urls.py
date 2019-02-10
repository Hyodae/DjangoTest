"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from community.views import *
from home.views import *

from django.conf.urls import include, url


urlpatterns = [

    # admin
    path('admin/', admin.site.urls),

    # community
    path('write/', write, name='write'),
    path('list/', list, name='list'),
    path('view/<int:num>/', view),

    # home : python example
    path('showimage.png/', showimage),  # matplotlib
    path('mplimage.png/', mplimage),    # matplotlib with numpy
    path('customer/', customer),        # mysql

    # music
    url(r'^music/', include('music.urls')),


]
