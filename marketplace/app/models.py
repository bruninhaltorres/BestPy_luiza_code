from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True, null=False, unique=True)
    nome_vendedor = models.CharField(max_length=200)
    login_vendedor = models.CharField(max_length=100)
    email_vendedor = models.EmailField()
    senha_vendedor = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.nome_vendedor

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True, null=False, unique=True)
    nome_produto = models.CharField(max_length=100)
    qtd_estoque = models.IntegerField()
    preco = models.FloatField()
    ativo = models.BooleanField(default=True)
    # vendedor = models.ForeignKey(User, on_delete=models.RESTRICT)
    #foto_produto = models.ImageField()

    def __str__(self):
        return str(self.id_produto)

    