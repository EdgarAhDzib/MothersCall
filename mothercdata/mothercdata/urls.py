from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('motherscnotes/', include('motherscnotes.urls')),
    path('', include('motherscnotes.index_url'),
    path('admin/', admin.site.urls),
]
