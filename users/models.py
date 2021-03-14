from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class UserDescricaoModel(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to='users/', null=True, blank=True)
    e_autor = models.BooleanField(default=False)
    descricao = models.TextField(max_length=280, null=True, blank=True)
