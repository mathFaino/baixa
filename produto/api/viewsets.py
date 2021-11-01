# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from produto.models import Produto
from .serializers import ProdutoSerializer, ProdutoSerializerList


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializerList
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('nome',)
    ordering_fields = ('id', 'nome')

    def get_serializer_class(self):
        actions = [
            'retrieve',
            'create',
            'update',
            'partial_update'
        ]
        if self.action in actions:
            return ProdutoSerializer
        return self.serializer_class
