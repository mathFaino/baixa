from rest_framework.serializers import ModelSerializer
from venda.models import Venda


class VendaSerializer(ModelSerializer):

    class Meta:
        model = Venda
        fields = (
            'data', 'hora', 'is_paid', 'cod_pagamento')
