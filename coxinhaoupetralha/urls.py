from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_tweets/$', views.get_tweets, name='get_tweets'),
]