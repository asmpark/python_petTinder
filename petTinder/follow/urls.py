from django.conf.urls import include,url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^/allUsers/$',views.allUsers,name='allUsers'),
]
