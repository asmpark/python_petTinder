from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^userpets/$',views.userpets,name='userpets'),
    url(r'^userpets/new/$',views.create_pet,name='create_pet'),
    url(r'^del_pet/(?P<pet_id>\d+)$',views.del_pet,name='del_pet'),
]
