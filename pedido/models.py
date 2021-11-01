from django.db import models
from item.models import Item
from carrinho.models import Carrinho


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    quantidade_vendida = models.FloatField()
    carrinho = models.ForeignKey(Carrinho,  related_name='pedidos', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
