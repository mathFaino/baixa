from django.db import models

from produto.models import Produto


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.FloatField()
    quantidade = models.FloatField()
    quant_min_venda = models.FloatField()
    quant_max_venda = models.FloatField(blank=True, null=True)
    data_fabricacao = models.DateField(blank=True, null=True)
    data_validade = models.DateField(blank=True, null=True)
    extra = models.TextField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
