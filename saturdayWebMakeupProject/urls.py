"""
URL configuration for saturdayWebMakeupProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views as gitau_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',gitau_views.home, name='home-url'),
    path('gallery/',gitau_views.gallery,name='gallery-url'),
    path('about/',gitau_views.about,name='about-url'),
    path('login/',gitau_views.login,name='login-url'),
    path('register/',gitau_views.register,name='register-url')

]
