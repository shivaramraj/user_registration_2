"""p29 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register/',Register,name='Register'),
    path('Home/',Home,name='Home'),
    path('User_login/',User_login,name='User_login'),
    path('User_logout/',User_logout,name='User_logout'),
    path('Display_profile/',Display_profile,name='Display_profile'),
    path('Change_password/',Change_password,name='Change_password'),
    path('forgetpassword/',forgetpassword,name='forgetpassword'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
