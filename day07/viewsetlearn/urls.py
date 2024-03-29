"""day07 URL Configuration

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
from viewsetlearn import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register('student', views.StuViewset, 'student')
router.register('class', views.ClsViewset, 'class')

urlpatterns = [
    url(r'^clslist/', views.ClsViewset.as_view({'get': 'list'}), name='clslist'),
    url(r'^clssingle/(?P<pk>\d+)', views.ClsViewset.as_view({'get': 'retrieve'}), name='clssingle'),
    url(r'^stulist/', views.StuViewset.as_view({'get': 'list', 'post': 'create'}), name='stulist'),
    url(r'^stussingle/(?P<pk>\d+)', views.StuViewset.as_view({'get': 'retrieve',
                                                              'put': 'update',
                                                              'patch': 'partial_update',
                                                              'delete': 'destroy'}), name='stusingle'),
    url(r'^stushow/', views.StuShow.as_view({'get': 'list'})),
    # url(r'', include(router.urls)),
]
