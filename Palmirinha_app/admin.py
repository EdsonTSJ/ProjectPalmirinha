from django.contrib import admin
from Palmirinha_app.models import Receita, Categoria
# Register your models here.

class ReceitaAdmin(admin.ModelAdmin):
    list_display=[ 'id', 'nome','categoria', 'dificuldade']
    list_display_links = ['id', 'nome']
    list_filter =['dificuldade','categoria']
    search_fields= ['nome']

class CategoriaAdmin(admin.ModelAdmin):
    list_display =['id','nome']
    list_display_links=['id','nome']
    search_fields=['nome']

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Categoria, CategoriaAdmin)