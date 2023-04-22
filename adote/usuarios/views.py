from django.shortcuts import render
from django.http import HttpResponse
# o django tem um arquivo chamado models que são os arquivos de BD
from django.contrib.auth.models import User
from django.contrib import messages
#importanto as messages 
from django.contrib.messages import constants
#serve pra autenticar o usuário, verificar se ele existe no BD. O djjango tem uma função de autenticar. E a outra é a função de login do django e a outra de logout
from django.contrib.auth import authenticate, login, logout
#serve pra redirecionar o user de uma url para outra
from django.shortcuts import redirect

def cadastro(request):
    # essa parte aqui autentica se o usuário já está logado, se estiver, não pode mostrar a pg de cadastro
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    elif request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':

        # dados vindo atraves da requisição post. O .get(nome) pega especificamente um tipo de informação, sem ele, pegaria todas as infos  
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        # print(nome, email, senha, confirmar_senha)


        #verificar se o usuário preencheu os campos. Strip tira os espaços em branco tanto do começo quanto do fim
        #render com a request faz voltar p pagina de cadastro
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'preencha todos os campos')
            return render(request, 'cadastro.html')
        
        #se senha for diferente de confirmar senha, precisa voltar pra cadastro de novo e mostrar uma mensagem de erro
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'digite as senhas iguais')
            return render(request, 'cadastro.html')
        
        try:
            #cria pra mim um novo usuário
            #isso aqui vai salvar o usuário dentro do BD pra mim
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            #mensagem de sucesso
            messages.add_message(request, constants.SUCCESS, 'usuario criado com sucesso')
            return render(request, 'cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, 'erro interno do sistema')
            return render(request, 'cadastro.html')
            #mensagem de erro
        #objects serve para acessar os dados de User

# função que vai ser chamada nas urls
def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        # django, verifica pra mim se esse nome aqui é igual o username lá no BD e o mesmo com a senha E GUARDA NESSA VARIAVEL
        user = authenticate(username = nome,
                            password = senha)
        if user is not None:
            #Se o user existir, ou seja, não for none, eu vou logar
            login(request, user)
            # redireciona o user da pg login, para a pg novo pet
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
            return render(request, 'login.html')

        return HttpResponse(f'{nome} {senha}')
        # nesse caso, eu já recebi os dados, e eles já estão dentro da url. agora preciso saber se esses dados dão match com algum lá dentro do BD
        #preciso AUTENTICAR o usuario

def sair(request):
    logout(request)
    return redirect('/auth/login')