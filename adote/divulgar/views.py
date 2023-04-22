from django.shortcuts import render
from django.http import HttpResponse
# função de autenticação para só quem está logado poder acessar a view
from django.contrib.auth.decorators import login_required

# recebe a requisição
#temos que garantir que só quem vai acessar essa view são os usuários logados
@login_required
def novo_pet(request):
    # se o método de requisição for GET, mostre esse html
    if request.method == 'GET':
        return render(request, 'novo_pet.html')