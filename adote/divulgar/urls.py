from django.urls import path
# do core do meu projeto, importe as views
from . import views

# url dentro dos padrões
urlpatterns = [
    path('novo_pet/', views.novo_pet, name = 'novo_pet')
]