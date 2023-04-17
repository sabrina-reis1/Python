from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    senha = models.CharField(max_length=6)