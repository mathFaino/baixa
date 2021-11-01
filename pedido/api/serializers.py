import django.http
from rest_framework.serializers import ModelSerializer
from pedido.models import Pedido
from item.models import Item
from carrinho.models import Carrinho
from carrinho.api.serializers import CarrinhoSerializerCreate


class PedidoSerializerList(ModelSerializer):
    carrinho = CarrinhoSerializerCreate(required=False)

    class Meta:
        model = Pedido
        fields = (
            'id', 'quantidade_vendida', 'carrinho', 'item')

    def create(self, validated_data):
        print(validated_data.keys())
        pedido = None
        item_id = validated_data.get('item', None)
        # carrinho_id = validated_data.get('carrinho', None)
        carrinho_wid = validated_data.pop('carrinho')  # validated_data.get('carrinho', None)

        if item_id is not None:
            item = Item.objects.filter(id=item_id.id).first()
            # carrinho = Carrinho.objects.filter(id=carrinho_id.id).first()
            carrinho = Carrinho.objects.create(**carrinho_wid)
            carrinho.save()
            # objects.get(pedido.item)
            if item.quantidade >= validated_data['quantidade_vendida']:
                print('chegou aqui')
                validated_data['carrinho'] = carrinho
                print(validated_data)
                pedido = Pedido.objects.create(**validated_data)
                print('quase')
                pedido.save()
                baixa_estoque(item, carrinho, pedido)
            else:
                pass
        return pedido


from item.api.serializers import ItemSerializerDatail


class PedidoSerializer(ModelSerializer):
    item = ItemSerializerDatail()

    class Meta:
        model = Pedido
        fields = (
            'id', 'quantidade_vendida', 'item')


class PedidoSerializerUpdate(ModelSerializer):

    class Meta:
        model = Pedido
        fields = (
            'id', 'quantidade_vendida', 'carrinho', 'item')

    def update(self, instance, validated_data):
        id_pedido = instance.pk
        quantidade = validated_data.get('quantidade_vendida', None)
        pedido_antigo = Pedido.objects.filter(id=id_pedido).first()
        print(pedido_antigo.item)

        item = Item.objects.filter(id=pedido_antigo.item.id).first()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if pedido_antigo.quantidade_vendida != quantidade:
            dif = calcula_diferenca(quantidade, pedido_antigo.quantidade_vendida)
            baixa_estoque(item, instance.carrinho, instance, dif)

        instance.save()

        return instance

    def partial_update(self, instance, validated_data):
        id_pedido = instance.pk
        pedido_antigo = Pedido.objects.filter(id=id_pedido).first()
        print(pedido_antigo.item)
        quantidade = validated_data.get('quantidade_vendida', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if quantidade:
            item = Item.objects.filter(id=pedido_antigo.item.id).first()
            if pedido_antigo.quantidade_vendida != quantidade:
                dif = calcula_diferenca(quantidade, pedido_antigo.quantidade_vendida)
                baixa_estoque(item, instance.carrinho, instance, dif)

        instance.save()

        return instance

    # def destroy(self, instance, validated_data):
    #     print('id item: ', instance.item.id)
    #     item = Item.objects.filter(id=instance.item.id).first()
    #     print(item)
    #     print('id carrinho: ', instance.carrinho.id)
    #     carrinho = Carrinho.objects.filter(id=instance.carrinho.id).first()
    #     print(carrinho)
    #     baixa_estoque(item, carrinho, instance)
    #     instance.destroy()
    #     return instance.status()


def baixa_estoque(item, carrinho, pedido, dif=0, destroy=False):
    if dif == 0:
        if destroy:
            item.quantidade = item.quantidade + pedido.quantidade_vendida
            carrinho.valor = carrinho.valor - (pedido.quantidade_vendida * item.valor)
        else:
            item.quantidade = item.quantidade - pedido.quantidade_vendida
            carrinho.valor = carrinho.valor + (pedido.quantidade_vendida * item.valor)
    else:
        item.quantidade = item.quantidade - dif
        print(dif * item.valor)
        print(dif)
        carrinho.valor = carrinho.valor + (dif * item.valor)
    item.save()

    carrinho.save()


def calcula_diferenca(valor1, valor2):
    resultado = valor1 - valor2
    return resultado
