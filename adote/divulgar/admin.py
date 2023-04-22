from django.contrib import admin
#importa as tabelas de models da mesma forma que está na classe
from .models import Raca, Tag, Pet

# model = tabela no BD
# cadastrando tabelas do BD no admin
admin.site.register(Raca)
admin.site.register(Tag)
admin.site.register(Pet)
