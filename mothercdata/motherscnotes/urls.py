from django.urls import path
from mothercdata import settings

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('fauna/', views.FaunaAPI.as_view()),
]
