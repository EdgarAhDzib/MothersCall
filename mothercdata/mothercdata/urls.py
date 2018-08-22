from django.contrib import admin, staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path('motherscnotes/', include('motherscnotes.urls')),
    path('', include('motherscnotes.index_url')),
    path('admin/', admin.site.urls),
    # staticfiles(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

urlpatterns += staticfiles_urlpatterns()
