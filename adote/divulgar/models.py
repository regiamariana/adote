from django.db import models
# das models da pasta "auth", importa a tabela de usuários
from django.contrib.auth.models import User
#é aqui nessa página que eu crio as tabelas no meu bd, tbm chamadas de models
# criar uma classe para as raças
#isso aqui é basicamente: crie uma tabla no banco chamada raça e coloque uma coluna nome, etc
class Raca(models.Model):
    # crie uma coluna chamada raça, na qual o tipo de dado vai ser char (string do python)
    #dentro de char, precisa colocar o max lenght, que é o tanto de dado q a coluna vai aceitar
    raca = models.CharField(max_length=50)

    def __str__(self) :
        return self.raca

# informações sobre os pets
class Tag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self) :
        return self.tag

# tabela dos pets em si
class Pet(models.Model):
    # isso é uma tupla
    #quando salvar no BD, vai salvar apenas uma letra
    #metodo de compressao de dados
    choices_status = (('P', 'Para adoção'),
                        ('A', 'Adotado'))
    # chamando a coluna de usuários de dentro da tabela de Usuários em auth, fazendo uma relação entre tabela
    # BD relacional
    # pet x user
    # relação de 1 pra muitos, um unico usuário pode cadastrar vários pets, mas 1 pet só pode ser de um usuário
    #chave estrangeira que liga um unico usuário a vários pets mas não o contrário
    # no on_delete, está perguntando o que deve acontecer aos pets do usuário se o usuário for deletado do BD? No caso, não faça nada
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # é o tipo de dado de imagem dentro das models
    #alem disso, as fotos dos pets serão salvas num local especifico, dentro da pasta media que o python criou, e lá é para fazer o upload das fotos dentro de uma pasta específica "fotos_pets"
    foto = models.ImageField(upload_to='fotos_pets')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    # relação de muitos pra muitos, uma tag pra muitos pets e um pet pra muitas tags
    # many to many fields
    tags = models.ManyToManyField(Tag)
    # nesse caso é a mesma coisa que com usuário, precisa relacionar um doguinho a uma só raça e uma raça a varios doguinhos
    # no Raca com r maiusculo, esta chamando a classe
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    # choices ofecere opções do que colocar dentro do charfield
    #dentro de choices, informa quais vão ser as variáveis disponíveis para se usar dentro da coluna, no caso status
    status = models.CharField(max_length=1, choices=choices_status)

    def __str__(self):
        return self.nome

    #lembrar que sempre que cria uma tabela nova é -> make migrations e -> migrate
    #depois cadastra a tabela migrada no admin para poder manipular por lá