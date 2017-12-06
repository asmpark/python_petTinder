from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^allusers/$',views.allusers,name='allusers'),
    url(r'^otherpetlist/(?P<user_id>\d+)$',views.otherPetList,name='otherpetlist'),
    url(r'^clickfollow/(?P<follow_id>\d+)$',views.clickFollow,name='clickfollow'),
    url(r'^followinglist/$',views.followingList,name='followinglist'),
]
