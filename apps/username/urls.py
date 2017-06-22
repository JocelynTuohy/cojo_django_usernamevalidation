from django.conf.urls import url
from . import views
app_name = 'username'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate$', views.validate, name='validate'),
    url(r'^success$', views.success, name='success'),
]
