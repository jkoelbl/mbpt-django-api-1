"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^announcement/', include('api.announcements.urls')),
    url(r'^challenge/', include('api.challenges.urls')),
    url(r'^discussion/', include('api.discussions.urls')),
    url(r'^profile/', include('api.profiles.urls')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    path('', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
