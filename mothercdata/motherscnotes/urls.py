from django.urls import path
from mothercdata import settings

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('view/<str:categ>/', views.ViewAll.as_view()),
    path('getfields/<str:categ>/', views.TableFields.as_view()),
    path('post/<str:categ>/<int:_id>', views.ItemPost.as_view()),
    path('get/<str:categ>/<int:_id>', views.GetItem.as_view()),
    path('add/<str:categ>/', views.ItemAdd.as_view()),
    path('delete/<str:categ>/<int:_id>', views.ItemDelete.as_view()),
    path('menu/', views.CategMenu.as_view()),
]
