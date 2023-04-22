from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('/', include('paginainicial.url')),
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    # include serve para apontar para determinado app
    path('divulgar/', include('divulgar.urls')),
]
