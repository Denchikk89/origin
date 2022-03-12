from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='list'),
    path('about-us', views.about, name='about'),
    path('base', views.base, name='base'),
    path('create', views.create, name='create')
]
