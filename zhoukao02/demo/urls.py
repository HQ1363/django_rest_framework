"""zhoukao02 URL Configuration

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
from demo import views

# 7.	使用modelviewset和router完成路由绑定（10分）
router = DefaultRouter()
router.register(prefix='comlist', viewset=views.ComList, basename='comlist')
router.register(prefix='comsingle', viewset=views.ComSingle, basename='comsingle')
router.register(prefix='emplist', viewset=views.EmpList, basename='emplist')
router.register(prefix='empsingle', viewset=views.EmpSingle, basename='empsingle')

urlpatterns = [
    url('', include(router.urls))
]
