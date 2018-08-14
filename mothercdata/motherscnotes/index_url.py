from django.urls import path
from mothercdata import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
