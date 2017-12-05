from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^allusers/$',views.allusers,name='allusers'),
url(r'^otherPetList/(?P<username>\w{1,50})$',views.otherPetList,name='otherPetList'),
    url(r'^followingList/$',views.followingList,name='followingList'),
]
