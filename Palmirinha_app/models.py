from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)


    def __str__(self):
        return self.nome
    
class Receita(models.Model):
    Dificuldade =[
        ('FC','Facil'),
        ('MD','Médio'),
        ('DF','Dificil'),
        ('EX','Extremo')
    ]
    nome = models.CharField(max_length = 50)
    tempo_de_preparo = models.TimeField(max_length=4, blank=False, null=True, help_text='Horas:Minutos')
    ingredientes = models.TextField(max_length=8000)
    modo_de_preparo = models.TextField(max_length=8000)
    dificuldade = models.CharField(max_length=10, choices= Dificuldade)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creditos =models.CharField(max_length=30, blank=True, null=True,)
    fonte =models.CharField(max_length=50, blank=True, null=True)
    URL =models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
#HELP_TEXT
#CRUD