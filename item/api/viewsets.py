from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from item.models import Item
from .serializers import ItemSerializerDatail, ItemSerializer, ItemSerializerCreate


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializerDatail
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('produto__id',)
    ordering_fields = ('valor', 'quantidade')

    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update'
        ]
        if self.action == 'retrieve':
            return ItemSerializer
        if self.action in actions:
            return ItemSerializerCreate
        return self.serializer_class
