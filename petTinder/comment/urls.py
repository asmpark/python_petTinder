from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^writeComment/(?P<petid>\d+)$',views.writeComment,name='writeComment'),
    url(r'^showComment/(?P<id>\d+)$',views.showComment,name='showComment'),
]
