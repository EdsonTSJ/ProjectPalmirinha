from django.shortcuts import render
from Palmirinha_app.models import Receita, Categoria

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()

    context={
        'categorias' : categorias
    }
    return render(request, 'index.html', context)

def listar_receitas(request):
    receitas = Receita.objects.all()
    #dicionario para levar os dados para o template
    #buscar as receitas doas 
    context={
        'receitas' : receitas
    }
    #Qual template essa view vai retornar
    return render (request, 'receitas.html', context)
def detalhes_receita(request, id):
    #buscando a receita correspondente 
    receita = Receita.objects.get(id = id)

    context ={
        'receita' : receita
    } 
    return render (request, 'receita.html', context)
