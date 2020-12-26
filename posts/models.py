from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AssuntoModel(models.Model):
    assunto = models.TextField(max_length=20)

    def __str__(self):
        return self.assunto


class PostModel(models.Model):
    titulo = models.TextField(max_length=100)
    corpo = models.TextField(max_length=2000)
    assunto = models.ManyToManyField(AssuntoModel)
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.titulo


class ComentarioModel(models.Model):
    corpo = models.TextField(max_length=300)
    data_criacao = models.DateField(auto_now_add=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)