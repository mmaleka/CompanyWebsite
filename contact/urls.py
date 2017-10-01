from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from contact import views

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
            ]