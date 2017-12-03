from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^del_user/$',views.del_user,name='del_user'),
    url(r'^changePW/$',views.changePW,name='changePW'),
]
