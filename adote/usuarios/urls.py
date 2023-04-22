from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    # dentro de views, chamar a função "logar"
    path('login/', views.logar, name = 'login'),
    path('sair/', views.sair, name= 'sair'),
]