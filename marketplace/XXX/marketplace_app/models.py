from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MarketPlace_List(models.Model):
    id_produto = models.CharField(max_length=50)
    nome_produto = models.CharField(max_length=100)
    qtd_estoque = models.IntegerField()
    preco = models.IntegerField()
    foto_produto = models.ImageField()
    ativo = models.BooleanField(default=True)
    vendedor = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.id_produto)

    #class Meta:
        #dt_table = 'produtos'   