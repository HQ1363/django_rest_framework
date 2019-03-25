"""day04 URL Configuration

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
from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^typelist/', views.Typelist.as_view(), name='typelist'),
    url(r'^goodslist/', views.Goodslist.as_view(), name='goodslist'),
    url(r'^goodsingle/(?P<pk>\d+)', views.Goodsingle.as_view(), name='goodsingle'),
]
