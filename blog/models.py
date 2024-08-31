from django.db import models

# Create your models here.
class Gostos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    ranking = models.CharField(max_length=1)

class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    ranking_utilidade = models.CharField(max_length=1)

class Comidas(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    ranking = models.CharField(max_length=1)
    imagem = models.ImageField(upload_to='imagens/')