from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from pedido.models import Pedido
from item.models import Item
from carrinho.models import Carrinho
from .serializers import PedidoSerializerList, PedidoSerializer, PedidoSerializerUpdate, baixa_estoque


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializerList

    def get_serializer_class(self):
        actions = [
            'update',
            'partial_update',
        ]
        ret = 'retrieve'
        if self.action == ret:
            return PedidoSerializer
        if self.action in actions:
            return PedidoSerializerUpdate
        return self.serializer_class

    def destroy(self, request, pk=None):
        pedido = self.get_object()
        item = Item.objects.filter(id=pedido.item.id).first()
        print(item)
        print('id carrinho: ', pedido.carrinho.id)
        carrinho = Carrinho.objects.filter(id=pedido.carrinho.id).first()
        print(carrinho)
        baixa_estoque(item, carrinho, pedido, destroy=True)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


