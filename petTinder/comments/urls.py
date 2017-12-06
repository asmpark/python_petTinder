from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^comment/(?P<pet_id>\d+)$',views.comment,name='comment'),
    url(r'^del_com/(?P<com_id>\d+)$',views.del_com,name='del_com'),
    url(r'^edit_com/(?P<com_id>\d+)/(?P<pet_id>\d+)$',views.edit_com,name='edit_com'),
    url(r'^edit_comment_form/(?P<com_id>\d+)/(?P<pet_id>\d+)$',views.edit_comment_form,name='edit_comment_form'),
]
