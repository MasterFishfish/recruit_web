"""recruitment URL Configuration

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
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.authtoken import views
from users.views import Register
from users.views import Beta

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^offer/', include('backend.urls', namespace='backend', app_name = 'backend')),
    url(r'^me/', include('users.urls')),
    url(r'^register/', Register.as_view()),
    url(r'^beta/', Beta.as_view()),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^auth/', views.obtain_auth_token),
] #url(r'^offer/', include('backend.urls', namespace='backend', app_name = 'backend'))
