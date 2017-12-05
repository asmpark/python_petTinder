from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^userpets/$',views.userpets,name='userpets'),
    url(r'^userpets/new/$',views.create_pet,name='create_pet'),
    url(r'^del_pet/(?P<pet_id>\d+)$',views.del_pet,name='del_pet'),
    url(r'^edit_pet/(?P<pet_id>\d+)$',views.edit_pet,name='edit_pet'),
    url(r'^edit_this_pet/(?P<pet_id>\d+)$',views.edit_this_pet,name='edit_this_pet'),
]
