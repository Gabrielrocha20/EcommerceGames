from django.shortcuts import redirect
from produto.models import Variacao
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils import utils

from ..models import ItemPedido, Pedido
from ..serializers import (ItemPedidoSerializer, PedidoRegisterSerializer,
                           PedidoSerializer)


class DispatchLoginRequiredMixin:
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

class PagarAPIView(DispatchLoginRequiredMixin, RetrieveAPIView):
    # permission_classes = [IsAuthenticated,]
    queryset = Pedido.objects.all()
    lookup_field = 'pk'
    serializer_class = PedidoSerializer

class SalvarPedidoAPI(CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoRegisterSerializer

    def perform_create(self, serializer):
        items = self.request.data['items']
        subtotal = 0
        qtd_total = 0
        for item in items:
            qtd_total += 1
            subtotal += item['preco']
        if subtotal >= 250:
            frete = 0
        else:
            frete = 10 * qtd_total
        total = subtotal + frete
        pedido = serializer.save(total=total,
            qtd_total=qtd_total,
            subtotal=subtotal,
            frete=frete)
        for item in items:
            ItemPedido.objects.create(pedido=pedido, **item)

class PedidoApiList(ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticated]

class PedidoApiDetail(RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # permission_classes = [IsAuthenticated]

class ItemPedidoApiDetail(RetrieveAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    # permission_classes = [IsAuthenticated]