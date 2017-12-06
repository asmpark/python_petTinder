"""petTinder URL Configuration

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
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('django.contrib.auth.urls')),
    url(r'',include('registration.urls')),
    url(r'',include('swipe.urls')),
    url(r'',include('editprofile.urls')),
    url(r'',include('homepage.urls')),
    url(r'',include('petlist.urls')),
    url(r'',include('follow.urls')),
    url(r'',include('comment.urls')),
    url(r'^favicon\.ico$', favicon_view),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
