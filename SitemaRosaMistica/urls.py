from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   path('academico/', include('apps.academico.urls')),
   path('admin/', admin.site.urls),
]