from django.db import models


class Venda(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    is_paid = models.BooleanField(default=True)
    cod_pagamento = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)
