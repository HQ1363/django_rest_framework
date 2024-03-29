"""zhoukao03_2 URL Configuration

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
from django.contrib import admin
# 8.对项目添加接口文档功能，并且在接口文档中对接口进行调试
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo/', include('demo.urls', namespace='demo')),
    # 8.对项目添加接口文档功能，并且在接口文档中对接口进行调试
    url(r'^docs/', include_docs_urls(title='周考三')),
]
