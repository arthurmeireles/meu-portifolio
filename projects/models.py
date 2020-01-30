from django.db import models




# Create your models here.


class Projeto(models.Model):
    titulo = models.CharField(max_length= 255)
    descricao = models.CharField(max_length= 255)
    link = models.CharField(max_length= 255)
    arquivo = models.ImageField()
    
     