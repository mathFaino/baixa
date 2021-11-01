
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from produto.api.viewsets import ProdutoViewSet
from pedido.api.viewsets import PedidoViewSet
from carrinho.api.viewsets import CarrinhoViewSet
from item.api.viewsets import ItemViewSet
from venda.api.viewsets import VendaViewSet

router = routers.DefaultRouter()
router.register('produto', ProdutoViewSet)
router.register('pedido', PedidoViewSet)
router.register('carrinho', CarrinhoViewSet)
router.register('venda', VendaViewSet)
router.register('item', ItemViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
