from django.urls import path
from Palmirinha_app import views

urlpatterns =[
    #(caminho,    views correspondente,  nome url)
    path('', views.index, name='index'),
    path('receitas/', views.listar_receitas, name ='receitas'),
    path('receita/<int:id>', views.detalhes_receita, name='receita')
]

#para cada url do site coloco uma linha nessa lista urlpatterns 