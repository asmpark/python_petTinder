from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^userpets/$',views.userpets,name='userpets'),
]