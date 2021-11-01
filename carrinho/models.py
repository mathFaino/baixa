from django.db import models
from venda.models import Venda


class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.FloatField()
    venda = models.OneToOneField(Venda, on_delete=models.CASCADE, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.pk)
