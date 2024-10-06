from django.contrib import admin
from django.urls import include
from django.urls import path

#from apps.pokemon_api.views import index

urlpatterns = [
    path('api/', include('apps.pokemon_api.urls')),
    path('admin/', admin.site.urls),
]
