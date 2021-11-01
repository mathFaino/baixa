from rest_framework.serializers import ModelSerializer
from item.models import Item


class ItemSerializerCreate(ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id', 'valor', 'quantidade', 'quant_min_venda', 'quant_max_venda', 'data_fabricacao', 'data_validade', 'extra',
             'produto')


from produto.api.serializers import ProdutoSerializerList


class ItemSerializer(ModelSerializer):
    produto = ProdutoSerializerList(read_only=True)

    class Meta:
        model = Item
        fields = (
            'id', 'valor', 'quantidade', 'quant_min_venda', 'quant_max_venda', 'data_fabricacao', 'data_validade', 'extra',
            'produto')


class ItemSerializerDatail(ModelSerializer):
    produto = ProdutoSerializerList()

    class Meta:
        model = Item
        fields = (
            'id', 'valor', 'quantidade', 'quant_min_venda', 'quant_max_venda', 'produto',)
