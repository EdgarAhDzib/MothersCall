from django.urls import path
from mothercdata import settings

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('view/<str:categ>/', views.ViewAll.as_view()),
    path('faunapost/<int:_id>', views.FaunaPost.as_view()),
    path('get/<str:categ>/<int:_id>', views.GetItem.as_view()),
    path('faunaadd/', views.FaunaAdd.as_view()),
    path('delete/<str:categ>/<int:_id>', views.ItemDelete.as_view()),
]
