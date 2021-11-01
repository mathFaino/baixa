from rest_framework.viewsets import ModelViewSet
from carrinho.models import Carrinho
from .serializers import CarrinhoSerializerList, CarrinhoSerializerCreate, CarrinhoSerializer


class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializerList

    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update'
        ]
        if self.action in actions:
            return CarrinhoSerializerCreate

        if self.action == 'retrieve':
            return CarrinhoSerializer

        return self.serializer_class
