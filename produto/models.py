from django.db import models


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    url_icon = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk)