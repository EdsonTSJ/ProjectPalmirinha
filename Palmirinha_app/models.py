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
    #tempo_de_preparo = models.DecimalField(max_digits=2, decimal_digits=2)
    ingredientes = models.TextField(max_length=8000)
    modo_de_preparo = models.TextField(max_length=8000)
    dificuldade = models.CharField(max_length=10, choices= Dificuldade)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome