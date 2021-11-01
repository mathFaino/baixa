from __future__ import annotations
from rest_framework.serializers import ModelSerializer
# from drf_writable_nested.serializers import WritableNestedModelSerializer
from carrinho.models import Carrinho


class CarrinhoSerializerList(ModelSerializer):

    class Meta:
        model = Carrinho
        fields = (
            'id', 'valor', 'venda', 'pedidos')


class CarrinhoSerializerCreate(ModelSerializer):

    class Meta:
        model = Carrinho
        fields = (
            'id', 'valor', 'venda', )


from venda.api.serializers import VendaSerializer
# from pedido.api.serializers import PedidoSerializer


class CarrinhoSerializer(ModelSerializer):
    venda = VendaSerializer()
   # pedidos = PedidoSerializer(read_only=True, many=True)

    class Meta:
        model = Carrinho
        fields = (
            'id', 'valor', 'venda', 'pedidos')



'''
class CarrinhoSerializerCreate(WritableNestedModelSerializer):
    pedidos = PedidoSerializerList(many=True)

    class Meta:
        model = Carrinho
        fields = (
            'id', 'cliente', 'valor', 'venda', 'pedidos', 'comissao')

'''


'''
class CarrinhoSerializerCreate(ModelSerializer):
    pedidos = PedidoSerializerList(many=True)

    class Meta:
        model = Carrinho
        fields = (
            'id', 'cliente', 'valor', 'venda', 'pedidos', 'comissao')

    def create(self, validated_data):
        #pedidos = []
        # for a in validated_data['pedidos']:
        #    pedidos.append(a)
        resultado = Pedido.objects.create(**validated_data['pedidos'][0])
        # if pedidos:
        #    for pedido_map in pedidos:
        #        pedidos_res = Pedido.objects.create(pedido_map)
                # PedidoSerializerList.create(, pedido_map)
        #        if pedidos_res is not None:
        #            validated_data['pedidos'].append(pedidos_res)

        # validated_data['pedidos'] = pedidos_res
        # validated_data['pedidos'] = resultado
        del validated_data['pedidos']
        carrinho = Carrinho.objects.create(**validated_data)
        carrinho.save()
        pedido_it = Pedido.objects.filter(id=resultado.id).first()
        carrinho.pedidos.set(pedido_it)
        #carrinho.pedidos.add(pedidos_res)


        # if pedidos_res != '':
            # for pedido_salvo in pedidos_res:
                # carrinho.pedidos.add(Carrinho.objects.get(pedido_salvo))

        return carrinho
'''
