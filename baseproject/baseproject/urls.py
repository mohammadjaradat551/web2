"""
URL configuration for baseproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),#for django
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),
    path('property/', include('property.urls'), name='property'),
    path('blog/', include('blog.urls'), name='blog'),
    path('about/', include('about.urls'), name='about'),
    path('', include('home.urls'), name='home'),
    path('summernote/', include('django_summernote.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
#meby rong
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_URL)