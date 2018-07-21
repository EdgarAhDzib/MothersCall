from django.urls import path
from mothercdata import settings

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('fauna/', views.FaunaAPI.as_view()),
    path('view/<str:categ>/', views.ViewAll.as_view()),
    path('faunapost/<int:fauna_id>', views.FaunaPost.as_view()),
    path('get/fauna/<int:fauna_id>', views.FaunaItem.as_view()),
    path('faunaadd/', views.FaunaAdd.as_view()),
    path('delete/fauna/<int:fauna_id>', views.FaunaDelete.as_view()),
]
