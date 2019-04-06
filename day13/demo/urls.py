"""day13 URL Configuration

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
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'telcode', TelcodeShow, basename='telcode')
router.register(r'register', Register, basename='register')
router.register(r'login', Login, basename='login')
router.register(r'usershow', UserShow, basename='usershow')
router.register(r'ordershow', OrderShow, basename='ordershow')
router.register(r'goodstypeshow', GoodstypeShow, basename='goodstypeshow')
router.register(r'goodshow', GoodsShow, basename='goodshow')

urlpatterns = [
    url('', include(router.urls, namespace='demo')),
]
