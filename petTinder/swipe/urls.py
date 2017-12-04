from django.conf.urls import include,url
from django.conf.urls.static import static
#from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^swipe/$',views.index,name='index'),
    url(r'^like/(?P<pet_id>\d+)$', views.like, name='like'),
    url(r'^nah/(?P<pet_id>\d+)$', views.nah, name='nah'),
    url(r'^likedpets/$',views.likedpets,name='likedpets'),
]
