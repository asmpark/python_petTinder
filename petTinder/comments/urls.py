from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^comment/(?P<pet_id>\d+)$',views.comment,name='comment'),
    url(r'^del_com/(?P<com_id>\d+)$',views.del_com,name='del_com'),
]
