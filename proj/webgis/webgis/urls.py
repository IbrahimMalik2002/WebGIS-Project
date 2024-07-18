"""
URL configuration for webgis project.

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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from webapp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login),
    path('index.html', views.index),
    path('about.html', views.about),
    path('booking.html', views.booking),
    path('contact.html', views.contact),
    path('Login.html', views.Login, name='Login'),
    path('maps.html', views.maps),
    path('register.html', views.register, name='register'),
    path('registration_success.html', views.registration_success,
         name='registration_success'),
    path('logout.html', views.logout, name='logout'),
    path('webapp/', include('webapp.urls')),
    path('loggingin', views.loggingin, name='loggingin'),
    path('Login.html', views.Login, name='Login'),
]
