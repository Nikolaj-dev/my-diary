from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappeli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('FastNote.urls')),
]
